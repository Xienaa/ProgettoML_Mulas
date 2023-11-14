import sqlite3

conn = sqlite3.connect(r"./database/db.sqlite/shopping_trends.sqlite")


def secretget_all():
    cursor = conn.cursor()
    x = cursor.execute('SELECT * FROM shopping_trends')
    return x