import torch.nn as nn
class DDQNNetwork(nn.Module):
    def __init__(self,s,a):
        super().__init__(); self.fc=nn.Sequential(nn.Linear(s,512),nn.ReLU(),nn.Linear(512,256),nn.ReLU(),nn.Linear(256,a))
    def forward(self,x): return self.fc(x)
