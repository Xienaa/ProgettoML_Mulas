import sqlite3
import requests
import pandas as pd
from io import StringIO

# Connessione al database SQLite
conn = sqlite3.connect(r"./database/db.sqlite/shopping_trends.sqlite")
cursor = conn.cursor()

# Definizione dello schema per la tabella
schema_tabella = """
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

# Creazione della tabella
cursor.execute(f'CREATE TABLE IF NOT EXISTS shopping_trends ({schema_tabella})')

# URL del file CSV
csv_url = 'https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/shopping_trends.csv'

# Scaricamento del contenuto CSV e conversione in un oggetto simile a un file
response = requests.get(csv_url)
csv_content = StringIO(response.text)

# Lettura dei dati CSV e inserimento nella tabella
df = pd.read_csv(csv_content)
df.to_sql("shopping_trends", conn, if_exists='replace', index=False, dtype='TEXT')

# Conferma le modifiche
conn.commit()

# Seleziona e stampa i dati per verificarli
cursor.execute('SELECT * FROM shopping_trends')
for row in cursor.fetchall():
    print(row)

# Chiude la connessione
conn.close()
