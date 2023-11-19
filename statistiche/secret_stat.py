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
    try:
        cursor = conn.cursor()
        query = 'SELECT AVG([Purchase Amount (USD)]) FROM shopping_trends'
        cursor.execute(query)
        media_purchase_amount = cursor.fetchone()[0]
        print(f"Valore effettivamente estratto dalla colonna 'Purchase Amount': {media_purchase_amount}")

        if media_purchase_amount is not None and media_purchase_amount != 0:
            # Arrotonda la media del "Purchase Amount" a due cifre decimali
            media_purchase_amount_arrotondata = round(media_purchase_amount, 2)
            risultato = {
                'media_purchase_amount': media_purchase_amount_arrotondata,
                'messaggio': 'Calcolo della media del "Purchase Amount" avvenuto con successo.'
            }
            return risultato
        else:
            raise HTTPException(status_code=404, detail="Nessun dato trovato o spesa media uguale a zero nella colonna 'Purchase Amount'.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante il calcolo della media del 'Purchase Amount (USD)': {str(e)}")
