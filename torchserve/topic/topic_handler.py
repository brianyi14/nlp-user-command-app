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
				self.text_command = encodedNumpyData
				sentence_vector = numpy.asarray(encodedNumpyData)
				tensor_sentence = torch.tensor(sentence_vector)
				model_input = torch.unsqueeze(tensor_sentence,0)
				model_input = model_input.float()
				return model_input
		
		def postprocess(self, model_pred):
				index2label = {1: 'Project',0: 'Task'}
				pred = index2label[int(torch.argmax(model_pred,dim=-1))]
				payload = {'command': self.text_command}
				if pred == 'Project':
					r = requests.post("https://us-east1-ml.googleapis.com/v1/projects/user-command-nlp/models/project-action/versions/v1:predict", json = payload)
				else:
					r = requests.post("https://us-east1-ml.googleapis.com/v1/projects/user-command-nlp/models/task-action/versions/v1:predict", json = payload)
				response = r.json()
				action_pred = response['action']
				topic_action_pred = {'Topic': pred, 'Action': action_pred}
				topic_action_pred = json.dumps(topic_action_pred)
				return [topic_action_pred]