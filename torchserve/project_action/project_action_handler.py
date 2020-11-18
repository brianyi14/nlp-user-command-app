from ts.torch_handler.base_handler import BaseHandler
import torch
from sentence_vectorizer import vectorize_sentence


class ModelHandler(BaseHandler):
  def preprocess(self, data):
	  sentence = data.get("data")
  	return sentence_vectorizer(sentence)

  def postprocess(self, model_pred):
    index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]