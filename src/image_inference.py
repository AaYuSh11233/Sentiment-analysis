import torch
from torchvision import transforms
from PIL import Image

model = torch.load("models/image_model.pt", map_location=torch.device("cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((48, 48)),
    transforms.Grayscale(),
    transforms.ToTensor(),
])

classes = ["angry", "happy", "sad", "neutral"]

def predict_image(image_path):
    img = Image.open(image_path)
    img_t = transform(img)  # apply transform -> tensor
    img_t = img_t.unsqueeze(0)  # add batch dimension
    with torch.no_grad():
        output = model(img_t)  # output shape: (1, num_classes)
    pred = torch.argmax(output, dim=1).item()
    return classes[pred]
