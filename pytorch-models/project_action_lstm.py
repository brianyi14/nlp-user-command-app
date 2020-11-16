import torch 
from torch import nn

class TopicModeler(nn.Module):
  def __init__(self):
    super(TopicModeler,self).__init__()
    self.LSTM = nn.LSTM(300,100,batch_first = True)
    self.outputtopic = nn.Linear(100,5) 
    self.softmax = nn.LogSoftmax(dim=-1)

  def forward(self,input):
    output, (h_n,c_n) = self.LSTM(input)
    topic_output = self.outputtopic(h_n)
    prob_output = self.softmax(topic_output)
    return prob_output