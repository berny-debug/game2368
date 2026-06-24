#cis 2368 homework one
#Maxwell Bernstein
#Prof Peddoju

import creds
from sql import DBConnection, execute_query, execute_read_query

# connect to DB at start of program
mycreds = creds.creds()
con = DBConnection(mycreds.connectionstring, mycreds.username, mycreds.password, mycreds.database)

if con is None:
    print("Error: Could not connect to database. Check your credentials in creds.py")
    exit()


def add_game():
    global con
    print("\n=== Add New Board Game ===")
    gamename = input("Enter the name of the game: ")
    try:
        maxplayers = int(input("Enter the maximum number of players: "))
    except ValueError:
        print("Invalid number for maximum players")
        return
    result = input("Enter the result of the game (win/loss/draw): ")
    try:
        gameduration = int(input("Enter the duration of the game in minutes: "))
        maxscore = int(input("Enter the maximum score of the game: "))
    except ValueError:
        print("Invalid number for duration or max score")
        return

    # ensure connection is available
    try:
        if not con.is_connected():
            print("DB connection lost; reconnecting...")
            con = DBConnection(mycreds.connectionstring, mycreds.username, mycreds.password, mycreds.database)
            if con is None:
                print("Failed to reconnect to DB.")
                return
    except Exception:
        # if con is None or doesn't have is_connected
        con = DBConnection(mycreds.connectionstring, mycreds.username, mycreds.password, mycreds.database)
        if con is None:
            print("Failed to connect to DB.")
            return

    sql = "INSERT INTO boardgames (gamename, maxplayers, result, gameduration, maxscore) VALUES (%s, %s, %s, %s, %s)"
    params = (gamename, maxplayers, result, gameduration, maxscore)

    cursor = con.cursor()
    try:
        cursor.execute(sql, params)
        con.commit()
        print("Game added successfully!")
    except Exception as e:
        print(f"Error adding game: {e}")
    finally:
        cursor.close()

def output_all_games():
    print("\n=== All Board Games ===")
    sql = "SELECT * FROM boardgames"
    games = execute_read_query(con, sql)

    if not games:
        print("No games found.")
        return
    for game in games:
        print(f"ID: {game['id']}, Name: {game['gamename']}, Max Players: {game['maxplayers']}, Result: {game['result']}, Duration: {game['gameduration']} mins, Max Score: {game['maxscore']}")

def main_menu():
    while True:
        print("\n" + "="*40)
        print("Board Game Inventory Management")
        print("="*40)
        print("a - Add New Game")
        print("o - Output All Games")
        print("q - Quit")
        print("="*40)
        choice = input("Enter your choice: (a/o/q): ").strip().lower()

        if choice == 'a':
            add_game()
        elif choice == 'o':
            output_all_games()
        elif choice == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Welcome to the Board Game Inventory Management System!")
    main_menu()



