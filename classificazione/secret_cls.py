from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from PIL import Image
import torch
import io
from torchvision import transforms
from ultralytics import YOLO  # Import your YOLOv8 model module

app = FastAPI()

# Load the pre-trained YOLOv8 model
model = YOLO('yolov8n.pt')  # Replace with your YOLOv8 model constructor

# Load the checkpoint from Ultralytics
checkpoint = torch.load('/home/mals/ProgettoML_Mulas/classificazione/Adam01/runs/detect/AdamMulas01/weights/best.pt')

# Extract the state_dict from the Ultralytics DetectionModel
model_state_dict = checkpoint['model'].state_dict()

# Load the state_dict into your YOLOv8 model
model.load_state_dict(model_state_dict)

model.eval()

# Define image transformation
transform = transforms.Compose([
    transforms.Resize((640, 640)),  # Adjust size according to YOLOv8 input size
    transforms.ToTensor(),
])

# Define API input model
class ImageInput(BaseModel):
    file: UploadFile

@app.post("/predict")
async def predict_clothes(image: ImageInput = File(...)):
    contents = await image.file.read()
    image_pil = Image.open(io.BytesIO(contents)).convert('RGB')
    image_tensor = transform(image_pil).unsqueeze(0)

    with torch.no_grad():
        # Assuming YOLOv8 output includes class indices, bounding boxes, and scores
        output = model(image_tensor)
        class_indices, _, _ = torch.nonzero(output['pred'][0][:, :, 4] > 0.5, as_tuple=True)

    # Assuming you have a function to map class indices to class names
    class_names = map_indices_to_names(class_indices)

    # Check if any of the detected classes are related to clothes
    clothes_classes = ['long sleeve dress', 'long sleeve outwear', 'long sleeve top', 'short sleeve dress',
                       'short sleeve outwear', 'short sleeve top', 'shorts', 'skirt', 'sling dress', 'sling',
                       'trousers', 'vest dress', 'vest']

    # Include any logic for class detection based on your specific use case
    detected_clothes = any(class_name in clothes_classes for class_name in class_names)

    # If clothes are detected, create or save in the appropriate folder
    if detected_clothes:
        # Create a folder if it doesn't exist
        folder_path = '/path/to/save/images/clothes'  # Replace with your desired path
        os.makedirs(folder_path, exist_ok=True)

        # Save the image in the folder with a unique name
        image_save_path = os.path.join(folder_path, f'{uuid.uuid4()}.jpg')
        image_pil.save(image_save_path)

        # Return the result as JSON
        return JSONResponse(content={"is_clothes": True, "saved_path": image_save_path})
    else:
        # Return the result as JSON indicating that the image is not clothes
        return JSONResponse(content={"is_clothes": False, "message": "L'immagine non è un vestito"})
