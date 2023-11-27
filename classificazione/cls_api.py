from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import cv2
import os
from ultralytics import YOLO

app = FastAPI()

# Percorso del modello YOLO
model_path = os.path.join('/home/mals/ProgettoML_Mulas/classificazione/Adam01/runs/detect/AdamMulas01/weights/last.pt')

# Carica il modello YOLO
model = YOLO(model_path)
threshold = 0.5

# Cartelle per salvare le immagini
clothes_folder = "clothes_images"
other_folder = "other_images"

# Crea le cartelle se non esistono
os.makedirs(clothes_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

@app.post("/uploadimage/")
async def create_upload_image(file: UploadFile = File(...)):
    # Salva il file caricato
    with open(file.filename, "wb") as f:
        f.write(file.file.read())

    # Carica il modello YOLO
    image = cv2.imread(file.filename)
    results = model(image)[0]

    is_clothes = False

    # Controlla se uno degli oggetti rilevati appartiene alla categoria "clothes"
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        # Controlla se l'oggetto rilevato è un tipo di abbigliamento
        if score > threshold and results.names[int(class_id)] in ["long sleeve dress", "long sleeve outwear", "long sleeve top", "short sleeve dress", "short sleeve outwear", "short sleeve top", "shorts", "skirt", "sling dress", "sling", "trousers", "vest dress", "vest"]:
            is_clothes = True
            break

    if is_clothes:
        # Salva l'immagine elaborata nella cartella "clothes_images"
        result_image_path = os.path.join(clothes_folder, f"result_{file.filename}")
        cv2.imwrite(result_image_path, image)
    else:
        # Fornisce l'output senza salvare l'immagine
        result_image_path = None

    # Restituisce una risposta JSON con il risultato
    return JSONResponse(content={"is_clothes": is_clothes, "result_image_path": result_image_path})
