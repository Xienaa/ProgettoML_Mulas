from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import io
import os

app = FastAPI()

# Carica il modello MobileNetV2 preaddestrato
model = MobileNetV2(weights="imagenet")

# Cartella in cui salvare le immagini di abbigliamento
clothing_folder = "clothing_images"

# Crea la cartella se non esiste
if not os.path.exists(clothing_folder):
    os.makedirs(clothing_folder)

# Funzione per classificare e salvare l'immagine
def classifica_vestiti(file: UploadFile = File(...)):
    # Leggi l'immagine come un oggetto PIL
    content = file.file.read()
    image = Image.open(io.BytesIO(content))

    # Ridimensiona l'immagine a dimensioni compatibili con MobileNetV2
    image = image.resize((224, 224))

    # Preprocessa l'immagine per adattarla al modello
    img_array = preprocess_input(np.array(image).reshape(1, 224, 224, 3))

    # Ottieni la predizione del modello
    predictions = model.predict(img_array)

    # Decodifica le predizioni
    decoded_predictions = decode_predictions(predictions)

    # Estrai il nome della classe predetta
    predicted_class = decoded_predictions[0][0][1]

    # Salva l'immagine nella cartella appropriata se è un capo di abbigliamento
    if "clothing" in predicted_class.lower():
        image_path = os.path.join(clothing_folder, file.filename)
        image.save(image_path)
        # Restituisci una risposta JSON con il messaggio e la classe predetta
        return JSONResponse(content={"message": "Immagine classificata come abbigliamento e salvata con successo", "predicted_class": predicted_class})
    else:
        # Restituisci una risposta JSON indicando che l'immagine non è un capo di abbigliamento
        return JSONResponse(content={"message": "Immagine non classificata come abbigliamento", "predicted_class": predicted_class})

