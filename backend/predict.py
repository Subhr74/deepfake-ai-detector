import torch
import cv2
from torchvision import transforms
from model import DeepfakeModel

model=DeepfakeModel()
model.eval()

transform=transforms.Compose([
transforms.ToPILImage(),
transforms.Resize((224,224)),
transforms.ToTensor()
])

def predict_image(path):

    img=cv2.imread(path)

    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    tensor=transform(img)

    tensor=tensor.unsqueeze(0)

    with torch.no_grad():

        output=model(tensor)

        prob=output.item()

    label="Fake" if prob>0.5 else "Real"

    return label,round(prob*100,2)