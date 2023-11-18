import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

conn = sqlite3.connect(r"./db.sqlite/shopping_trends.sqlite",check_same_thread=False)

class CustomerInput(BaseModel):
    customer_id: str
    age: int
    gender: str
    item_purchased: str
    category: str
    purchase_amount: float
    location: str
    size: str
    color: str
    season: str
    review_rating: float
    subscription_status: str
    payment_method: str
    shipping_type: str
    discount_applied: str
    promo_code_used: str
    previous_purchases: int
    preferred_payment_method: str
    frequency_of_purchases: str
class Customer:
    def __init__(self, customer_id, age, gender, item_purchased, category, purchase_amount, location, size, color, season, review_rating, subscription_status, payment_method, shipping_type, discount_applied, promo_code_used, previous_purchases, preferred_payment_method, frequency_of_purchases):
        self.customer_id = customer_id
        self.age = age
        self.gender = gender
        self.item_purchased = item_purchased
        self.category = category
        self.purchase_amount = purchase_amount
        self.location = location
        self.size = size
        self.color = color
        self.season = season
        self.review_rating = review_rating
        self.subscription_status = subscription_status
        self.payment_method = payment_method
        self.shipping_type = shipping_type
        self.discount_applied = discount_applied
        self.promo_code_used = promo_code_used
        self.previous_purchases = previous_purchases
        self.preferred_payment_method = preferred_payment_method
        self.frequency_of_purchases = frequency_of_purchases

    def to_dict(self):
        customer_dict = {
            "customer_id": self.customer_id,
            "age": self.age,
            "gender": self.gender,
            "item_purchased": self.item_purchased,
            "category": self.category,
            "purchase_amount": self.purchase_amount,
            "location": self.location,
            "size": self.size,
            "color": self.color,
            "season": self.season,
            "review_rating": self.review_rating,
            "subscription_status": self.subscription_status,
            "payment_method": self.payment_method,
            "shipping_type": self.shipping_type,
            "discount_applied": self.discount_applied,
            "promo_code_used": self.promo_code_used,
            "previous_purchases": self.previous_purchases,
            "preferred_payment_method": self.preferred_payment_method,
            "frequency_of_purchases": self.frequency_of_purchases
        }
        return customer_dict    
class CustomerUpdateInput(BaseModel):
    customer_id: str
    age: int = None
    gender: str = None
    item_purchased: str = None
    category: str = None
    purchase_amount: float = None
    location: str = None
    size: str = None
    color: str = None
    season: str = None
    review_rating: int = None
    subscription_status: str = None
    payment_method: str = None
    shipping_type: str = None
    discount_applied: str = None
    promo_code_used: str = None
    previous_purchases: int = None
    preferred_payment_method: str = None
    frequency_of_purchases: str = None

def secretget_all():
    cursor = conn.cursor()
    x=cursor.execute('SELECT * FROM shopping_trends').fetchall()
    result_list = [(Customer(*i).to_dict()) for i in x]
    return result_list

def secretget_by_id(customer_id):
    cursor = conn.cursor()
    query = 'SELECT * FROM shopping_trends WHERE UPPER("Customer ID") = UPPER(?)'
    x = cursor.execute(query, (str(customer_id).strip('{}'),)).fetchall()
    result_list = [(Customer(*i).to_dict()) for i in x]
    return result_list

def secretdelete(customer_id):
    cursor = conn.cursor()

# Stampa il valore di customer_id prima dell'operazione. 
# l'ho fatto per capire meglio dei problemi che avevo durante la creazione della funzione
    print(f"Valore di customer_id prima dell'eliminazione: {customer_id}")

# Elimina le righe corrispondenti
    cursor.execute('DELETE FROM shopping_trends WHERE UPPER("Customer ID") = UPPER(?)', (str(customer_id).strip('{}'),))
    conn.commit()

# Controlla il numero di righe eliminate
    if cursor.rowcount == 0:
        print("Nessuna riga eliminata con il customer_id specificato")
        return  {"Operazione": "Nessuna riga eliminata con il customer_id specificato"}

# Stampa un messaggio dopo l'eliminazione
    print("Eliminazione effettuata")

    return {"Operazione": "Eliminazione avvenuta con successo!"}


def create_user(customer_id, age, gender, item_purchased, category, purchase_amount, location, size, color, season, review_rating, subscription_status, payment_method, shipping_type, discount_applied, promo_code_used, previous_purchases, preferred_payment_method, frequency_of_purchases):
    
    cursor = conn.cursor()
# Esegui l'inserimento dei dati nella tabella 'shopping_trends'
    cursor.execute('INSERT INTO shopping_trends ("Customer ID", "Age", "Gender", "Item Purchased", "Category", "Purchase Amount (USD)", "Location", "Size", "Color", "Season", "Review Rating", "Subscription Status", "Payment Method", "Shipping Type", "Discount Applied", "Promo Code Used", "Previous Purchases", "Preferred Payment Method", "Frequency of Purchases") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (customer_id, age, gender, item_purchased, category, purchase_amount, location, size, color, season, review_rating, subscription_status, payment_method, shipping_type, discount_applied, promo_code_used, previous_purchases, preferred_payment_method, frequency_of_purchases))

# Effettua il commit delle modifiche nel database
    conn.commit()

# Restituisci un messaggio di successo
    return {"Operazione": "Aggiunta avvenuta con successo!"}


def create_user_in_function(customer_data: CustomerInput):
    try:
# Richiama 'create_user' con i dati forniti da 'customer_data'
        result = create_user(**customer_data.dict())
        return result
    except Exception as e:
# Gestisce eventuali errori sollevando un'eccezione HTTP con un messaggio dettagliato
# Fatto sempre per capire meglio dei problemi avuti al riguardo
        raise HTTPException(status_code=500, detail=f"Errore durante la creazione dell'utente: {str(e)}")


def secretupdate(update_data: CustomerUpdateInput):
    cursor = conn.cursor()

    # Costruisci la query di aggiornamento dinamicamente
    update_query = 'UPDATE shopping_trends SET '
    update_query += ', '.join([f'"{key}" = ?' for key, value in update_data.dict().items() if value is not None])
    update_query += ' WHERE "Customer ID" = ?'

    # Costruisci la tupla dei valori da aggiornare
    values_to_update = [value for value in update_data.dict().values() if value is not None]
    values_to_update.append(update_data.customer_id)

    # Esegui la query di aggiornamento
    cursor.execute(update_query, tuple(values_to_update))
    conn.commit()

    # Restituisci un messaggio di successo
    return {"Operazione": "Aggiornamento avvenuto con successo!"}


