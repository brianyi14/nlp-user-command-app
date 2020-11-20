import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote
import numpy as np
from gensim import models
import gensim.downloader as api
from spellchecker import SpellChecker

class EchoRequest(messages.Message):
    message = messages.StringField(1)


class EchoResponse(messages.Message):
    """A proto Message that contains a simple string field."""
    message = messages.StringField(1)


ECHO_RESOURCE = endpoints.ResourceContainer(
    EchoRequest,
    n=messages.IntegerField(2, default=1))

@endpoints.api(name='vectorizer', version='v1')
class VectorizerApi(remote.Service):
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        ECHO_RESOURCE,
        # This method returns an Echo message.
        EchoResponse,
        path='echo',
        http_method='POST',
        name='echo')
    def echo(self, request):
        sentence = request.message
        stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]  
	    cleaned_sentence = ''
  	    for char in sentence:
  		    if char.isalpha() or char == ' ':
      		    cleaned_sentence += char
    	    if char == '-':
      		    cleaned_sentence += ' '
        spell_checker = SpellChecker()
  	    sentence_lst = cleaned_sentence.split()
  	    num_words = len(sentence_lst)
  	    sentence_vector = np.zeros((10,300))
  	    for i in range(num_words):
		    word = sentence_lst[i]
    	    if word not in stopwords:
      		    try:
        		    vectorized_word = np.zeros(300)
      		    except KeyError:
        		    misspelled = spell_checker.unknown([word])
        	    corrected_word = None
        	    for word in misspelled:
          		    corrected_word = spell_checker.correction(word)
        	    try:
          		    vectorized_word = np.zeros(300)
        	    except KeyError:
          		    vectorized_word = np.zeros(300)
    	    else:
      	    #stop word is empty vector of 0s
      		    vectorized_word = np.zeros(300)
    	    sentence_vector[i] = vectorized_word
  		    for j in range(num_words,10,1):
    		    sentence_vector[j] = np.zeros(300)
        output_message = sentence_vector.tostring()
        return EchoResponse(message=output_message)

api = endpoints.api_server([VectorizerApi])
