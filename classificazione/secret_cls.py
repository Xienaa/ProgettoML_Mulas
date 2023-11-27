from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import cv2
import os
from ultralytics import YOLO

app = FastAPI()

model_path = os.path.join('/home/mals/ProgettoML_Mulas/classificazione/Adam01/runs/detect/AdamMulas01/weights/last.pt')

model = YOLO(model_path)
threshold = 0.5

clothes_folder = "clothes_images"
other_folder = "other_images"

# Create folders if they don't exist
os.makedirs(clothes_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

@app.post("/uploadimage/")
async def create_upload_image(file: UploadFile = File(...)):
    # Save the uploaded file
    with open(file.filename, "wb") as f:
        f.write(file.file.read())

    # Load the YOLO model
    image = cv2.imread(file.filename)
    results = model(image)[0]

    is_clothes = False

    # Check if any of the detected objects belong to the "clothes" category
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold and results.names[int(class_id)] in ["long sleeve dress", "long sleeve outwear", "long sleeve top", "short sleeve dress", "short sleeve outwear", "short sleeve top", "shorts", "skirt", "sling dress", "sling", "trousers", "vest dress", "vest"]:
            is_clothes = True
            break

    if is_clothes:
        # Save the processed image in the "clothes_images" folder
        result_image_path = os.path.join(clothes_folder, f"result_{file.filename}")
        cv2.imwrite(result_image_path, image)
    else:
        # Provide output without saving the image
        result_image_path = None

    return JSONResponse(content={"is_clothes": is_clothes, "result_image_path": result_image_path})

