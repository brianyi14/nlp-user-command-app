import torch 
from torch import nn

#LSTM architecture that takes input of vectorized sentences and outputs probability for each topic
class TopicModeler(nn.Module):
  def __init__(self):
    """input size: length of a word vector"""
    """hidden_size: number of nodes in hidden layer for LSTM unit"""
    """output_size: number of possible outputs or labels for the model"""

    super(TopicModeler,self).__init__()
    #intialize LSTM model with parameters
    self.LSTM = nn.LSTM(300,100,batch_first = True)
    #fully connected linear layer between last hidden state of LSTM and output predictions
    self.output2topic = nn.Linear(100,5)
    #softmax layer that converts the outputs into probability distribution and then logs those probabilities 
    self.softmax = nn.LogSoftmax(dim=-1)

  #function for forward pass through model
  def forward(self,input):
    output, (h_n,c_n) = self.LSTM(input)
    input last hidden state through linear layer
    topic_output = self.output2topic(h_n)
    prob_output = self.softmax(topic_output)
    return input