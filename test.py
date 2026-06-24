#test.py 

import creds
from sql import DBConnection, execute_read_query

mycreds = creds.creds()
con = DBConnection(mycreds.connectionstring, mycreds.username, 
                   mycreds.password, mycreds.database)

if con:
    print("Connected to server!")
    sql = "SHOW DATABASES;"
    databases = execute_read_query(con, sql)
    
    print("\n📋 Available Databases:")
    for db in databases:
        print(db)

    

        