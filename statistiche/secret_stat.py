import sqlite3
from fastapi import HTTPException
from pydantic import BaseModel


conn = sqlite3.connect(r"../database/db.sqlite/shopping_trends.sqlite",check_same_thread=False)

def calcola_eta_media_da_db():

    cursor = conn.cursor()
    query = 'SELECT AVG("Age") FROM shopping_trends'
    cursor.execute(query)
    eta_media = cursor.fetchone()[0]
    # Arrotonda l'età media a tre cifre decimali
    eta_media_arrotondata = round(eta_media, 3)
    risultato = {
        'eta_media': eta_media_arrotondata,
        'messaggio': 'Calcolo dell\'età media avvenuto con successo.'
    }
    return risultato


def calcola_spesa_media_da_db():
    cursor = conn.cursor()
    query = 'SELECT AVG("Purchase Amount") FROM shopping_trends'
    cursor.execute(query)
    spesa_media = cursor.fetchone()[0]
    
    print(f"Spesa media prima dell'arrotondamento: {spesa_media}")

    spesa_media_arrotondata = round(spesa_media, 2)

    risultato = {
        'spesa_media': spesa_media_arrotondata,
        'messaggio': 'Calcolo della spesa media avvenuto con successo.'
    }

    return risultato