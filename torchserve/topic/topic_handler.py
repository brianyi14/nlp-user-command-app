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
				header = {'Authorization': 'Bearer ya29.a0AfH6SMBFzv0VcXiEULX0sR4BOj02oOxmP1Jd4Ctlc2hqJP9jkZrzJJp2gFBtvoSVZhVp-FiO7gADDfh8R8pjhuPWE7UErMeBldaI4KU0RV-0Gch09c0s31fnSStS3eCx7O0a23BnjJCXW29vpz0vS6bfQl8g-DCV2hH6m4NMZjr9UqbDg5tUPn5S44gcH9Ijwlb4Np-uTDohziAWsQLWoa6bvjfN5g_Z2awdZvjsZwI3A4pSqL8inWeBEOHzxNc5dOfNhv6fbmv_1tv-OWVKBA'}
				if pred == 'Project':
					r = requests.post("http://localhost:8080/predictions/lstm_project_action", json = payload,headers=header)
				else:
					r = requests.post("http://localhost:8080/predictions/lstm_task_action", json = payload,headers=header)
				response = r.json()
				action_pred = response['action']
				topic_action_pred = {'Topic': pred, 'Action': action_pred}
				topic_action_pred = json.dumps(topic_action_pred)
				return [topic_action_pred]