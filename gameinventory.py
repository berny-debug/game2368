#cis 2368 homework one
#Maxwell Bernstein
#Prof Peddoju

import creds
from sql import DBConnection, execute_query, execute_read_query

# connect to DB at start of program
mycreds = creds.creds()
con = DBConnection(mycreds.connectionstring, mycreds.username, mycreds.password, mycreds.database)


def add_game():
    print("\n=== Add New Board Game ===")
    gamename = input("Enter the name of the game: ")
    maxplayers = int(input("Enter the maximum number of players: "))
    result = input("Enter the result of the game (win/loss/draw): ")
    gameduration = int(input("Enter the duration of the game in minutes: "))
    maxscore = int(input("Enter the maximum score of the game: "))

    