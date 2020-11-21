import endpoints
from endpoints import message_types
from endpoints import messages
from endpoints import remote
import numpy as np
from gensim import models
import gensim.downloader as api
from spellchecker import SpellChecker

# [START endpoints_echo_api_messages]
class EchoRequest(messages.Message):
    message = messages.StringField(1)


class EchoResponse(messages.Message):
    """A proto Message that contains a simple string field."""
    message = messages.StringField(1)


ECHO_RESOURCE = endpoints.ResourceContainer(
    EchoRequest,
    n=messages.IntegerField(2, default=1))
# [END endpoints_echo_api_messages]


# [START endpoints_echo_api_class]
@endpoints.api(name='echo', version='v1')
class EchoApi(remote.Service):

    # [START endpoints_echo_api_method]
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        ECHO_RESOURCE,
        # This method returns an Echo message.
        EchoResponse,
        path='echo',
        http_method='POST',
        name='echo')
    def echo(self, request):
        output_message = ' '.join([request.message] * request.n)
        return EchoResponse(message=output_message)
    # [END endpoints_echo_api_method]

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        ECHO_RESOURCE,
        # This method returns an Echo message.
        EchoResponse,
        path='echo/{n}',
        http_method='POST',
        name='echo_path_parameter')
    def echo_path_parameter(self, request):
        sentence = request.message
		spell_checker = SpellChecker()
  		sentence_lst = sentence.split()
  		num_words = len(sentence_lst)
  		sentence_vector = np.zeros((10,300))
  		for i in range(num_words):
    		word = sentence_lst[i]
    		if word not in stopwords:
      			try:
        			vectorized_word = vectorizer.wv[word]
      			except:
        			misspelled = spell_checker.unknown([word])
        		corrected_word = None
        		for word in misspelled:
          			corrected_word = spell_checker.correction(word)
        			try:
          				vectorized_word = vectorizer.wv[corrected_word]
        			except:
          				vectorized_word = np.zeros(300)
    		else:
      			vectorized_word = np.zeros(300)
    		sentence_vector[i] = vectorized_word
  		for j in range(num_words,10,1):
    		sentence_vector[j] = np.zeros(300)
  		output_message = sentence_vector.tostring()
        return EchoResponse(message=output_message)

# [START endpoints_api_server]
api = endpoints.api_server([EchoApi])
# [END endpoints_api_server]
