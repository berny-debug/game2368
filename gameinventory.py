#cis 2368 homework one
#Maxwell Bernstein
#Prof Peddoju

import creds
from sql import DBConnection, execute_query, execute_read_query

# connect to DB at start of program
mycreds = creds.creds()
con = DBConnection(mycreds.connectionstring, mycreds.username, mycreds.password, mycreds.database)
