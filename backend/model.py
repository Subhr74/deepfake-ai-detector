import torch
import torch.nn as nn
import torchvision.models as models

class DeepfakeModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.model=models.resnet18(weights="DEFAULT")

        self.model.fc=nn.Linear(self.model.fc.in_features,1)

    def forward(self,x):

        x=self.model(x)

        return torch.sigmoid(x)