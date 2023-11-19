import sqlite3
from fastapi import HTTPException
from pydantic import BaseModel


conn = sqlite3.connect(r"../database/db.sqlite/shopping_trends.sqlite",check_same_thread=False)

def calculate_average_age_from_db():
    cursor = conn.cursor()
    query = 'SELECT AVG("Age") FROM shopping_trends'
    cursor.execute(query)
    average_age = cursor.fetchone()[0]
    return average_age