from ts.torch_handler.base_handler import BaseHandler
import torch

class ModelHandler(BaseHandler):
  def preprocess(self, data):
    return torch.randn(1,10,300).float()

  def postprocess(self, model_pred):
    index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]