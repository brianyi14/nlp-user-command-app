import torch
from torch import nn

class SimpleModel(nn.Module):
  def __init__(self):
    super(SimpleModel,self).__init__()
    self.llayer = nn.LSTM(300,100,batch_first = True)

  def forward(self,x):
    return self.llayer(x)