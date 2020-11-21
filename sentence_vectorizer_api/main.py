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


ECHO_RESOURCE = endpoints.ResourceContainer(EchoRequest,n=messages.IntegerField(2, default=1))

@endpoints.api(name='vectorizer', version='v1')
class VectorizerApi(remote.Service):
    @endpoints.method(ECHO_RESOURCE,EchoResponse,path='echo',http_method='POST',name='echo')
    def echo(self, request):
        sentence = request.message
        stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]  
	    output_message = len(sentence)
        return EchoResponse(message=output_message)

api = endpoints.api_server([VectorizerApi])
