from flask import Flask, request, jsonify
import products_dao
import uom_dao
import orders_dao
import json
from sql_connection import get_sql_connection


app = Flask(__name__)

connection = get_sql_connection()

###Products_Table

@app.route('/getProducts', methods = ['GET']) #http://127.0.0.1:5000/hello - server hello acts as an endpoint of the webpage #get method is to get data from server
def get_products():   
    products = products_dao.get_all_products(connection)
    response = jsonify(products) #converts to json to put into web page
    response.headers.add('Access-Control-Allow-Origin','*') #it is also known as course policy
    return response

@app.route('/deleteProduct', methods = ['POST']) #post updates data into server
def delete_product():
    return_id = products_dao.delete_product(connection, request.form[('product_id')])
    response = jsonify({
        'product_id': return_id
        })
    response.headers.add('Access-Control-Allow-Origin','*') #it is also known as course policy
    return response

@app.route('/insertProduct', methods = ['POST'])
def insert_product():
    request_payload = json.loads(request.form['data']) #to convert form data from string back to dictionary
    product_id = products_dao.insert_products(connection, request_payload)
    response = jsonify({
        'product_id' : product_id
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/editProduct', methods = ['POST','GET'])
def edit_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.edit_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

####UOM_Table

@app.route('/getUOM', methods = ['GET']) 
def get_uom():   
    uom = uom_dao.get_uoms(connection)
    response = jsonify(uom) #converts to json to put into web page
    response.headers.add('Access-Control-Allow-Origin','*') #it is also known as course policy
    return response

@app.route('/insertUOM', methods = ['POST'])
def insert_uom():
    request_payload = json.loads(request.form['data'])
    uom_id = uom_dao.insert_uom(connection, request_payload)
    response = jsonify({
        'uom_id': uom_id
        })
    response.headers.add('Access-Control-Allow-Origin','*') #it is also known as course policy
    return response


####Orders_Table

@app.route('/insertOrder', methods = ['POST'])
def insert_order():
    request_payload = json.loads(request.form['data']) #to convert form data from string back to dictionary
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id' : order_id
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getAllOrders', methods = ['GET']) #http://127.0.0.1:5000/hello - server hello acts as an endpoint of the webpage #get method is to get data from server
def get_orders():   
    orders = orders_dao.get_all_orders(connection)
    response = jsonify(orders) #converts to json to put into web page
    response.headers.add('Access-Control-Allow-Origin','*') #it is also known as course policy
    return response

@app.route('/getOrderDetails', methods = ['GET'])
def get_order_details():
    order_id = int(request.args.get('orderid'))
    response = orders_dao.get_order_details(connection, order_id)
    
    
    # request_payload = json.loads(request.form['order_id'])
    # order_details = orders_dao.get_order_details(connection, request_payload)
    # response = jsonify(order_details)
    
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response




if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)


