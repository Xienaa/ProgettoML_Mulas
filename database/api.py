from flask import Flask, jsonify, request
import sqlite3
import pandas as pd

app = Flask(__name__)

DATABASE_PATH = "/home/mals/Desktop/ProgettoML_Mulas/database/db.sqlite/shopping_trends.sqlite"

# Create
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        data = request.get_json()
        cursor.execute('''
            INSERT INTO customers ("Customer ID", Age, Gender, "Item Purchased", Category, "Purchase Amount (USD)", Location, 
                                   Size, Color, Season, "Review Rating", "Subscription Status", "Payment Method", 
                                   "Shipping Type", "Discount Applied", "Promo Code Used", "Previous Purchases", 
                                   "Preferred Payment Method", "Frequency of Purchase") 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data['Customer ID'], data['Age'], data['Gender'], data['Item Purchased'], data['Category'], 
              data['Purchase Amount (USD)'], data['Location'], data['Size'], data['Color'], data['Season'], 
              data['Review Rating'], data['Subscription Status'], data['Payment Method'], data['Shipping Type'], 
              data['Discount Applied'], data['Promo Code Used'], data['Previous Purchases'], 
              data['Preferred Payment Method'], data['Frequency of Purchase']))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Customer created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Read all customers
@app.route('/customers', methods=['GET'])
def read_all_customers():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM customers')
        customers = cursor.fetchall()

        conn.close()

        return jsonify({'customers': customers}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Read a specific customer
@app.route('/customers/<int:customer_id>', methods=['GET'])
def read_customer(customer_id):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM customers WHERE "Customer ID"=?', (customer_id,))
        customer = cursor.fetchone()

        conn.close()

        if customer:
            return jsonify({'customer': customer}), 200
        else:
            return jsonify({'message': 'Customer not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update a specific customer
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        data = request.get_json()
        cursor.execute('''
            UPDATE customers 
            SET Age=?, Gender=?, "Item Purchased"=?, Category=?, "Purchase Amount (USD)"=?, Location=?, 
                Size=?, Color=?, Season=?, "Review Rating"=?, "Subscription Status"=?, "Payment Method"=?, 
                "Shipping Type"=?, "Discount Applied"=?, "Promo Code Used"=?, "Previous Purchases"=?, 
                "Preferred Payment Method"=?, "Frequency of Purchase"=?
            WHERE "Customer ID"=?
        ''', (data['Age'], data['Gender'], data['Item Purchased'], data['Category'], 
              data['Purchase Amount (USD)'], data['Location'], data['Size'], data['Color'], data['Season'], 
              data['Review Rating'], data['Subscription Status'], data['Payment Method'], data['Shipping Type'], 
              data['Discount Applied'], data['Promo Code Used'], data['Previous Purchases'], 
              data['Preferred Payment Method'], data['Frequency of Purchase'], customer_id))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Customer updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a specific customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('DELETE FROM customers WHERE "Customer ID"=?', (customer_id,))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Customer deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
