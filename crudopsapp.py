import mysql.connector
import creds

from mysql.connector import Error
from sql import DBConnection
from sql import execute_query
from sql import execute_read_query

#connect to DB
mycreds = creds.creds()
con = DBConnection(mycreds.connectionstring, mycreds.username, mycreds.password, mycreds.database)

#Create/Insert
sql ="insert into users(fname, lname, email) values('suresh2', 'peddoju2', 'test2@uh.edu')"
execute_query(con, sql)

val1="suresh4"
val2="peddoju4"
val3="test4@uh.edu"
sql ="insert into users(fname, lname, email) values('%s', '%s', '%s')" % (val1, val2, val3)
execute_query(con, sql)

#Read
sql="select * from users"
allusers=execute_read_query(con, sql)
print(allusers)

for eachuser in allusers:
    print(eachuser)

#Update
uid=4
sql="update users set email='test5@uh.edu' where id=%s" % (uid)
execute_query(con, sql)

#Delete
uid=4
sql="delete from users where id=%s" % (uid)
execute_query(con, sql)


