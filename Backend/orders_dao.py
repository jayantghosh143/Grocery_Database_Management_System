from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO orders"
                   "(customer_name, total, datetime)"
                   "VALUES(%s, %s, %s)")
    order_data = (order['customer_name'], order['total'], datetime.now())
    cursor.execute(order_query, order_data) #in execute always goes first query the data to be passed
    order_id = cursor.lastrowid #gives last row id after insertion of the row
    
    
    order_details_query = ("INSERT INTO order_details"
                   "(order_id, product_id, quantity, total_price)"
                   "VALUES(%s, %s, %s, %s)")
    order_details_data = []
    for order_detail_record in order['order_details']: 
        order_details_data.append([ ##this set of data should be a list
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
            ])
        
    cursor.executemany(order_details_query, order_details_data)  #many is there to execute many queries at once
        
    
    
    connection.commit() #necessary after doing changes to the database
    
    return order_id


def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    
    response = []
    for (order_id,customer_name,total,date_time) in cursor:
        response.append({
            'order_id':order_id,
            'customer_name':customer_name,
            'total':total,
            'datetime':date_time
            })
    return response


def get_order_details(connection, order_id):
    cursor = connection.cursor()
    query = ("SELECT orders.customer_name as customer, products.product_name as product, products.price_per_unit, quantity, total_price"
             " from order_details "
             "inner join orders on order_details.order_id = orders.order_id "
             "inner join products on order_details.product_id = products.product_id "
             "WHERE order_details.order_id = "+str(order_id))
    
    cursor.execute(query)
    
    response = []
    
    for (customer, product, price_per_unit, quantity, total_price) in cursor:
        response.append({
            'customer' : customer,
            'product' : product,
            'price_per_unit' : price_per_unit,
            'quantity' : quantity,
            'total_price' : total_price
            })
        
    return response
    



if __name__ == '__main__':

    connection = get_sql_connection()
    # print(insert_order(connection,{
    #     'customer_name' : 'Mohan Kumar',
    #     'total' : '160',
    #     'order_details' : [
    #             {
    #             'product_id' : 1,
    #             'quantity' : 2,
    #             'total_price' : 40
    #             },
    #             {
    #             'product_id' : 2,
    #             'quantity' : 2,
    #             'total_price' : 120
    #             }
    #             ]
        
    #     }))
    
    # print(get_all_orders(connection))
    
    print(get_order_details(connection, 11))