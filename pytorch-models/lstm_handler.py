from ts.torch_handler.base_handler import BaseHandler
import torch
from torch import nn
import numpy as np
from spellchecker import SpellChecker


class ModelHandler(BaseHandler):
  def preprocess(self, data):
  	#path = api.load("word2vec-google-news-300", return_path=True)
  	#w = models.KeyedVectors.load_word2vec_format(path, binary=True)
  	stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]  
  	#cleaned_sentence = ''
  	#for char in sentence:
  		#if char.isalpha() or char == ' ':
      		#cleaned_sentence += char
    	#if char == '-':
      		#cleaned_sentence += ' '
    #spell_checker = SpellChecker()
  	sentence_lst = data.split()
  	num_words = len(sentence_lst)
  	sentence_vector = np.zeros((max_len,300))
  	for i in range(num_words):
    	word = sentence_lst[i]
    	if word not in stopwords:
    		vectorized_word = np.random.rand(300)
      		#try:
        		#vectorized_word = w.wv[word]
      		#except KeyError:
        		#misspelled = spell_checker.unknown([word])
        	#corrected_word = None
        	#for word in misspelled:
          		#corrected_word = spell_checker.correction(word)
        	#try:
          		#vectorized_word = w.wv[corrected_word]
        	#except KeyError:
          		#vectorized_word = np.zeros(300)
    	else:
      	#stop word is empty vector of 0s
      		vectorized_word = np.zeros(300)
    	sentence_vector[i] = vectorized_word
  		for j in range(num_words,max_len,1):
    		sentence_vector[j] = np.zeros(300)
    tensor_sentence = torch.tensor(sentence_vector)
    model_input = torch.unsqueeze(tensor_sentence,0)
    model_input = model_input.float()
    return model_input

  def postprocess(self, model_pred):
    index2label = {0: 'Create',1: 'On Target',2: 'At Risk',3: 'Danger',4: 'Completed'}
    return [index2label[int(torch.argmax(model_pred,dim=-1))]]