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
	    output_message = len(sentence)
        return EchoResponse(message=output_message)

api = endpoints.api_server([VectorizerApi])
