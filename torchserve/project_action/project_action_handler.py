from ts.torch_handler.base_handler import BaseHandler
import torch
import numpy as np
from gensim import models
from spellchecker import SpellChecker

class ModelHandler(BaseHandler):
  def preprocess(self, data):
  	#path = api.load("word2vec-google-news-300", return_path=True)
  	#w = models.KeyedVectors.load_word2vec_format(path, binary=True)
  	stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]  
	  sentence = data.get("data")
    sentence_lst = sentence.split()
    #cleaned_sentence = ''
  	#for char in sentence:
  		#if char.isalpha() or char == ' ':
      		#cleaned_sentence += char
    	#if char == '-':
      		#cleaned_sentence += ' '
    #spell_checker = SpellChecker()
  	#sentence_lst = cleaned_sentence.split()
  	num_words = len(sentence_lst)
  	sentence_vector = np.zeros((max_len,300))
  	for i in range(num_words):
      vectorized_word = np.zeros(300)
    	sentence_vector[i] = vectorized_word
  	for j in range(num_words,10,1):
    	sentence_vector[j] = np.zeros(300)
    tensor_sentence = torch.tensor(sentence_vector)
    model_input = torch.unsqueeze(tensor_sentence,0)
    model_input = model_input.float()
    return model_input

  def postprocess(self, model_pred):
    index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]