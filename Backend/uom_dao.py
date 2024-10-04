def get_uoms(connection):
    cursor = connection.cursor()
    query = ("SELECT * from uom")
    cursor.execute(query)
    
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id' : uom_id,
            'uom_name' : uom_name
            })
    return response

def insert_uom(connection, uom):
    cursor = connection.cursor()
    query = f"INSERT INTO uom (uom_name) VALUES ('{uom['uom_name']}');"
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    from sql_connection import get_sql_connection
    
    connection = get_sql_connection()
    #print(get_uoms(connection))
    # print(insert_uom(connection,{
    #     'uom_name':'cubic-meter'
    #     }))