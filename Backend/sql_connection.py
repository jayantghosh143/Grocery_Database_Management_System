import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    
    if __cnx is None:
        __cnx = mysql.connector.connect(user = 'Jayant', password= 'Deepasha@24',
                                          host = '127.0.0.1',
                                          database = 'grocery_store_dbms')
    
    return __cnx
