import os
from fastapi import File, UploadFile, FastAPI
from secret_cls import ImageInput, Image, transform, torch,model, , JSONResponse, 
# Inizializza l'app FastAPI
app = FastAPI()

