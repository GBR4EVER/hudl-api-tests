import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:myserver.database.windows.net'
database = 'hudldb'
username = 'cburkley'
password = 'passsword'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

def fetch_all_rows(query):
    conn = cnxn
    curs = conn.cursor()
    curs.execute(query)
    cache_rows = curs.fetchall()
    curs.close()
    conn.close()
    return cache_rows