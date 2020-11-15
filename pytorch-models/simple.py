import torch
from torch import nn

class SimpleModel(nn.Module):
  def __init__(self):
    super(SimpleModel,self).__init__()
    self.llayer = nn.Linear(5,1)
    nn.init.xavier_uniform(self.llayer.weight)

  def forward(self,x):
    return self.llayer(x)