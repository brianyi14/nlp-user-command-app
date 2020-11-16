from ts.torch_handler.base_handler import BaseHandler
import torch
from torch import nn

#from gensim import models
#import gensim.downloader as api
#from spellchecker import SpellChecker

#path = api.load("word2vec-google-news-300", return_path=True)
class ModelHandler(BaseHandler):
  def preprocess(self, data):
    #w = models.KeyedVectors.load_word2vec_format(path, binary=True)
    #vectorized_sentence = self.vectorize_sentence(sentence)
    #tensor_sentence = torch.tensor(vectorized_sentence)
    #model_input = torch.unsqueeze(vectorized_sentence,0)
    #model_input = model_input.float()
    #return model_input
    return torch.zeros(1,10,300).float()

  def postprocess(self, model_pred):
    index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]