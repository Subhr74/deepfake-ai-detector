import torch
import torchvision
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
from model import DeepfakeModel
import torch.nn as nn
import torch.optim as optim

transform=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

dataset=datasets.ImageFolder("dataset",transform=transform)

loader=DataLoader(dataset,batch_size=16,shuffle=True)

model=DeepfakeModel()

criterion=nn.BCELoss()

optimizer=optim.Adam(model.parameters(),lr=0.0001)

for epoch in range(5):

    for images,labels in loader:

        labels=labels.float().unsqueeze(1)

        outputs=model(images)

        loss=criterion(outputs,labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

    print("Epoch",epoch,"Loss:",loss.item())

torch.save(model.state_dict(),"deepfake_model.pth")