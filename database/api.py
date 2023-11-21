from fastapi import FastAPI
from secret import (
    secret_update,
    secretget_all,
    secretget_by_id,
    secret_delete,
    create_user_in_function,
    CustomerInput,
    
)

# Inizializza l'app FastAPI
app = FastAPI()

# Endpoint per ottenere tutti i dati
@app.get("/shoptrends")
def get_all():
    all_data = secretget_all()
    return all_data

# Endpoint per ottenere dati in base all'ID del cliente
@app.get("/shoptrendsbyid/{customer_id}")
def getbyid(customer_id: int):
    select_data = secretget_by_id(customer_id)
    return select_data

# Endpoint per eliminare un cliente in base all'ID
@app.delete("/deletecustomer/{customer_id}")
def delete(customer_id: int):
    delete_user = secret_delete({customer_id})
    return delete_user

# Endpoint per creare un nuovo utente
@app.post("/createuser")
async def create_user_endpoint(customer_data: CustomerInput):
    return create_user_in_function(customer_data)

# Endpoint per aggiornare un utente esistente in base all'ID
@app.put("/updateuser/{customer_id}")
async def update_user_endpoint(customer_id: int, update_data: CustomerInput):
    update_data.customer_id = customer_id
    ret = secret_update(update_data)
    return ret
