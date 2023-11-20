import sqlite3
from fastapi import HTTPException
import pandas as pd

conn = sqlite3.connect(r"../database/db.sqlite/shopping_trends.sqlite", check_same_thread=False)

def apri_connessione_database():
    return sqlite3.connect(r"../database/db.sqlite/shopping_trends.sqlite", check_same_thread=False)

def calcola_eta_media_da_db():
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante il calcolo dell'età media: {str(e)}")

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

async def calcola_mediana_previous_purchases():
    try:
        # Apri la connessione al database
        conn_db = apri_connessione_database()

        # Esegui la query e carica i risultati in un DataFrame pandas
        query = 'SELECT [Previous Purchases] FROM shopping_trends'
        df = pd.read_sql_query(query, conn_db)

        if not df.empty:
            # Calcola la mediana dei valori nella colonna 'Previous Purchases'
            mediana_previous_purchases = df['Previous Purchases'].median()

            # Arrotonda la mediana a due cifre decimali
            mediana_previous_purchases_arrotondata = round(mediana_previous_purchases, 2)

            risultato = {
                'mediana_previous_purchases': mediana_previous_purchases_arrotondata,
                'messaggio': 'Calcolo della mediana di "Previous Purchases" avvenuto con successo.'
            }
            return risultato
        else:
            raise HTTPException(status_code=404, detail="Nessun dato trovato nella colonna 'Previous Purchases'.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante il calcolo della mediana di 'Previous Purchases': {str(e)}")
    finally:
        # Chiudi la connessione al database alla fine
        conn_db.close()


async def calcola_distribuzione_percentuale():
    try:
        # Apri la connessione al database
        conn_db = apri_connessione_database()

        # Esegui la query e carica i risultati in un DataFrame pandas
        query = 'SELECT [Frequency of Purchases] FROM shopping_trends'
        df = pd.read_sql_query(query, conn_db)

        if not df.empty:
            # Rimuovi spazi extra e converti tutto in minuscolo
            cleaned_text = df['Frequency of Purchases'].str.strip().str.lower()

            # Rimuovi eventuali spazi vuoti rimasti dopo la pulizia
            cleaned_text = cleaned_text.replace('', pd.NA)

            # Sostituisci "Every 3 Months" con un placeholder
            cleaned_text = cleaned_text.str.replace('every 3 months', 'every_3_months')

            # Sostituisci i numeri con un placeholder
            cleaned_text = cleaned_text.str.replace(r'\b\d+\b', 'numberplaceholder', regex=True)

            # Dividi il testo in parole
            words = cleaned_text.str.split()

            # Sostituisci il placeholder con il numero originale
            words = words.apply(lambda w: [word.replace('numberplaceholder', '') for word in w])

            # Unisci le parole in un unico elenco di parole
            flattened_words = words.explode()

            # Sostituisci il placeholder con la parola originale
            flattened_words = flattened_words.replace('every_3_months', 'every 3 months')

            # Calcola le frequenze delle parole
            word_counts = flattened_words.value_counts()

            # Calcola la distribuzione percentuale in termini percentuali
            percentage_distribution = (word_counts / word_counts.sum()) * 100

            # Rimuovi eventuali valori nulli dovuti a spazi vuoti
            percentage_distribution = percentage_distribution.dropna()

            # Arrotonda i valori a 3 numeri dopo la virgola
            percentage_distribution = percentage_distribution.round(3)

            # Aggiungi il simbolo % agli output
            percentage_distribution_with_percent = percentage_distribution.apply(lambda x: f"{x}%")

            risultato = {
                'distribuzione_percentuale': percentage_distribution_with_percent.to_dict(),
                'messaggio': 'Calcolo della distribuzione percentuale avvenuto con successo.'
            }
            return risultato
        else:
            raise HTTPException(status_code=404, detail="Nessun dato trovato nella colonna 'Frequency of Purchases'.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante il calcolo della distribuzione percentuale: {str(e)}")
    finally:
        # Chiudi la connessione al database alla fine
        conn_db.close()