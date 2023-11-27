import torch
from torchvision import models, transforms
from PIL import Image

# Carica il modello addestrato
model = models.resnet50(pretrained=False)
model.fc = torch.nn.Linear(2048, 13)  # Supponendo che il tuo modello abbia 13 classi

# Carica i pesi addestrati
model.load_state_dict(torch.load('percorso/al/tuo/modello.pth'))
model.eval()

# Definisci la trasformazione dell'immagine
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Funzione per prevedere la classe di un'immagine
def predict_class(image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image)
    image = image.unsqueeze(0)  # Aggiungi la dimensione del batch

    with torch.no_grad():
        output = model(image)
    
    _, predicted_class = torch.max(output, 1)
    return predicted_class.item()