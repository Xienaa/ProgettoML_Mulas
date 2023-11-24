from fastapi import FastAPI, File, UploadFile
from secret_cls import (classifica_vestiti)
# Inizializza l'app FastAPI
app = FastAPI()

# Endpoint per l'upload delle immagini
@app.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    # Chiama la funzione di classificazione e ritorna la risposta
    return classifica_vestiti(file)
