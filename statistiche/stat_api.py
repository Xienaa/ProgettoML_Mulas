from fastapi import FastAPI
from secret_stat import calcola_eta_media_da_db,calcola_spesa_media_da_db,calcola_mediana_previous_purchases

app = FastAPI()

@app.get("/average_age")
async def calculate_average_age_endpoint():
    average_age = calcola_eta_media_da_db()
    return {"average_age": average_age}

@app.get("/importo_medio_acquisto")
async def calcola_importo_medio_acquisto():
    importo_medio_acquisto = calcola_spesa_media_da_db()
    return {"importo_medio_acquisto": importo_medio_acquisto} 

@app.get("/calcola_mediana_previous_purchases")
async def api_calcola_mediana_previous_purchases():
    mediana_previous_purchases = await calcola_mediana_previous_purchases()
    return {"mediana_previous_purchases": mediana_previous_purchases}