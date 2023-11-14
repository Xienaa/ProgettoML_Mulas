import sqlite3
import pandas as pd

conn = sqlite3.connect(r"/home/mals/Desktop/ProgettoML_Mulas/database/db.sqlite/shopping_trends.sqlite")


stud_data = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/shopping_trends.csv')

stud_data.to_sql("shopping_trends", conn, if_exists='replace', index=False)

cursor = conn.cursor()

for row in cursor.execute('SELECT * FROM shopping_trends'):
    print(row)

conn.close()