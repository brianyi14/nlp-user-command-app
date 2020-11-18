from ts.torch_handler.base_handler import BaseHandler
import torch
from sentence_vectorizer import vectorize_sentence


class ModelHandler(BaseHandler):
  def preprocess(self, data):
  	sentence = data.get("data")
  	return sentence_vectorizer(sentence)

  def postprocess(self, model_pred):
    index2label = {0: 'Task',1: 'Project'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]