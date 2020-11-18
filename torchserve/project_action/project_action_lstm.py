import torch
from torch import nn

class ProjectActionModel(nn.Module):
  def __init__(self):
    super(ProjectActionModel,self).__init__()
    self.lstm = nn.LSTM(300,100,batch_first = True)
    self.outputtopic = nn.Linear(100,5)
    self.softmax = nn.LogSoftmax(dim=-1)

  def forward(self,x):
    output, (h_n,c_n) = self.lstm(x)
    outputt = self.outputtopic(h_n)
    prob_output = self.softmax(outputt)
    return prob_output