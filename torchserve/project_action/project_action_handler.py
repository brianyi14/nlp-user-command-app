from ts.torch_handler.base_handler import BaseHandler
import torch
import numpy
import requests
import json

class ModelHandler(BaseHandler):
		def preprocess(self, data):
				request_data = data[0]
				request_data = request_data['body']
				text_command = request_data['command']
				payload = {'command':text_command}
				r = requests.post("https://user-command-nlp.ue.r.appspot.com", json = payload)
				response = r.json()
				encodedNumpyData = response['array']
				sentence_vector = numpy.asarray(encodedNumpyData)
				tensor_sentence = torch.tensor(sentence_vector)
				model_input = torch.unsqueeze(tensor_sentence,0)
				model_input = model_input.float()
				return model_input
		
		def postprocess(self, model_pred):
				index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
				return [index2label[int(torch.argmax(model_pred,dim=-1))]]