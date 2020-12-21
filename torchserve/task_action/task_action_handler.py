from ts.torch_handler.base_handler import BaseHandler
import torch
import numpy
import requests
import json

#comment
class ModelHandler(BaseHandler):
		def preprocess(self, data):
				request_data = data[0]
				request_data = request_data['body']
				if request_data.get('test',0) != 0:
					tensor_sentence = torch.randn(10,300)
				else:
					text_command_array = request_data['command']
					sentence_vector = numpy.asarray(text_command_array)
					tensor_sentence = torch.tensor(sentence_vector)
				model_input = torch.unsqueeze(tensor_sentence,0)
				model_input = model_input.float()
				return model_input
		
		def postprocess(self, model_pred):
				index2label = {0: 'To Do',1: 'In Progress',2:'In Review',3:'Blocked',4:'Completed'}
				if float(torch.max(model_pred)) >= -0.46:
					action = index2label[int(torch.argmax(model_pred,dim=-1))]
				else:
					action = 'NA'
				pred = {'action': action}
				pred = json.dumps(pred)
				return [pred]