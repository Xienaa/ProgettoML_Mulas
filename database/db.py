import sqlite3
import requests
import pandas as pd
from io import StringIO

# Connect to the SQLite database
conn = sqlite3.connect(r"./database/db.sqlite/shopping_trends.sqlite")
cursor = conn.cursor()

# Define the schema for the table
stud_data = """
    Customer_ID INTEGER,
    Age INTEGER,
    Gender TEXT,
    Item_Purchased TEXT,
    Category TEXT,
    Purchase_Amount REAL,
    Location TEXT,
    Size TEXT,
    Color TEXT,
    Season TEXT,
    Review_Rating INTEGER,
    Subscription_Status TEXT,
    Payment_Method TEXT,
    Shipping_Type TEXT,
    Discount_Applied TEXT,
    Promo_Code_Used TEXT,
    Previous_Purchases INTEGER,
    Preferred_Payment_Method TEXT,
    Frequency_of_Purchases INTEGER
"""

# Create the table
cursor.execute(f'CREATE TABLE IF NOT EXISTS shopping_trends ({stud_data})')

# URL of the CSV file
csv_url = 'https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/shopping_trends.csv'

# Download CSV content and convert it to a file-like object
response = requests.get(csv_url)
csv_content = StringIO(response.text)

# Read CSV data and insert into the table
df = pd.read_csv(csv_content)
df.to_sql("shopping_trends", conn, if_exists='replace', index=False, dtype='TEXT')

# Commit the changes
conn.commit()

# Select and print the data to verify
cursor.execute('SELECT * FROM shopping_trends')
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
