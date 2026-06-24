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
    print("\n=== Add New Board Game ===")
    gamename = input("Enter the name of the game: ")
    maxplayers = int(input("Enter the maximum number of players: "))
    result = input("Enter the result of the game (win/loss/draw): ")
    gameduration = int(input("Enter the duration of the game in minutes: "))
    maxscore = int(input("Enter the maximum score of the game: "))

    sql = "INSERT INTO boardgames (gamename, maxplayers, result, gameduration, maxscore) VALUES ('%s', %d, '%s', %d, %d)" % (gamename, maxplayers, result, gameduration, maxscore)

    # parameterized query
    cursor = con.cursor()
    try:
        cursor.execute(sql, (gamename, maxplayers, result, gameduration, maxscore))
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
        while true:
            print("/n" + "="*40)
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



