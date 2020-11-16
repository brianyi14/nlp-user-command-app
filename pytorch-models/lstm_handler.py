from ts.torch_handler.base_handler import BaseHandler
import torch
from torch import nn
import numpy as np
from gensim import models
import gensim.downloader as api
from spellchecker import SpellChecker


class ModelHandler(BaseHandler):

  def postprocess(self, model_pred):
    index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]