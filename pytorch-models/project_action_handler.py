from ts.torch_handler.base_handler import BaseHandler
import torch
from torch import nn
import numpy as np
from spellchecker import SpellChecker
from sentence_vectorizer import vectorize_sentence


class ModelHandler(BaseHandler):
  def preprocess(self, data):
	sentence = data.get("data")
  	sentence_vector = sentence_vectorizer(sentence)
    tensor_sentence = torch.tensor(sentence_vector)
    model_input = torch.unsqueeze(tensor_sentence,0)
    model_input = model_input.float()
    return model_input

  def postprocess(self, model_pred):
    index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]