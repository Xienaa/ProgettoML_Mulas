from flask import Flask, jsonify, request
import sqlite3
import pandas as pd

app = Flask(__name__)

DATABASE_PATH = "/home/mals/Desktop/ProgettoML_Mulas/database/db.sqlite/shopping_trends.sqlite"

# Calculate mean age
@app.route('/mean_age', methods=['GET'])
def calculate_mean_age():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT AVG(Age) FROM shopping_trends')
        mean_age = cursor.fetchone()[0]

        conn.close()

        return jsonify({'mean_age': mean_age}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Calculate mean purchase amount
@app.route('/mean_purchase_amount', methods=['GET'])
def calculate_mean_purchase_amount():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT AVG("Purchase Amount (USD)") FROM shopping_trends')
        mean_purchase_amount = cursor.fetchone()[0]

        conn.close()

        return jsonify({'mean_purchase_amount': mean_purchase_amount}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Calculate median previous purchases
@app.route('/median_previous_purchases', methods=['GET'])
def calculate_median_previous_purchases():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT MEDIAN("Previous Purchases") FROM shopping_trends')
        median_previous_purchases = cursor.fetchone()[0]

        conn.close()

        return jsonify({'median_previous_purchases': median_previous_purchases}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Calculate percentage distribution of purchase frequencies
@app.route('/percentage_distribution', methods=['GET'])
def calculate_percentage_distribution():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('SELECT "Frequency of Purchases", COUNT(*) FROM shopping_trends GROUP BY "Frequency of Purchases"')
        frequencies = cursor.fetchall()

        total_records = sum([record[1] for record in frequencies])
        percentage_distribution = {record[0]: (record[1] / total_records) * 100 for record in frequencies}

        conn.close()

        return jsonify({'percentage_distribution': percentage_distribution}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
