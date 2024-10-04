from sql_connection import get_sql_connection #importing this from other module

def get_all_products(connection):
    
    cursor = connection.cursor() #cursor allows to execute queries
    
    query = ("SELECT products.product_id, products.product_name, products.uom_id, products.price_per_unit, uom.uom_name "  
    "FROM products inner join uom on products.uom_id = uom.uom_id")
     
    cursor.execute(query) #after this all thngs will get inside cursor
    
    response = [] #storing all things in list as dictionary objects 
    
    for (product_id, product_name, uom_id, price_per_unit,uom_name) in cursor: #tuple is our column names
        response.append(
                {
                    'product_id' : product_id,
                    'product_name' : product_name,
                    'uom_id' : uom_id,
                    'price_per_unit' : price_per_unit,
                    'uom_name' : uom_name
                }
            )
    
    return response


def insert_products(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products"
             "(product_name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    
    cursor.execute(query,data)
    connection.commit() #this is necessary to commit the changes to SQL Table
    
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    
def edit_product(connection, product):
    cursor = connection.cursor()
    query = ("UPDATE products "
             "SET product_name = %s, uom_id = %s, price_per_unit = %s"
             " WHERE product_id = %s")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'], product['product_id'])
    cursor.execute(query, data)
    connection.commit()
    return product['product_id']
    
if __name__ == '__main__':
    connection = get_sql_connection()
    # print(delete_product(connection, 10))
    #print(get_all_products(connection))
    print(edit_product(connection, {
        'product_id': 1,
        'product_name': 'Tea',
        'uom_id': 1,
        'price_per_unit': 25
        }))
