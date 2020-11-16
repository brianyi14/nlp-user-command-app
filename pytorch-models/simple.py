import torch
from torch import nn

class SimpleModel(nn.Module):
  def __init__(self):
    super(SimpleModel,self).__init__()
    self.llayer = nn.LSTM(300,100,batch_first = True)
    self.outputtopic = nn.Linear(100,5)
    self.softmax = nn.LogSoftmax(dim=-1)

  def forward(self,x):
    outputo = self.llayer(x)
    outputt = self.outputtopic(outputo)
    prob_output = self.softmax(outputt)
    return prob_output