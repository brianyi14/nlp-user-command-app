import numpy as np
from gensim import models
import gensim.downloader as api
from spellchecker import SpellChecker
import json
from json import JSONEncoder
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

#specify the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#class that encodes a numpy array into a JSON object 
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

#load the pretrained Google Word2Vec model that is saved in the data folder 
vectorizer = models.KeyedVectors.load_word2vec_format(
    "./data/google-word2vec.bin", binary=True)

#creates the POST method for the app which tells Flask how to handle POST requests to the API endpoint
@app.route('/', methods=['POST'])
@cross_origin()
def home():
    #load the request data which is in JSON format
    data = request.get_json()
    #the JSON object contains a command key which has the text command
    sentence = data['command']
    #iterate over the text command and remove any special characters
    cleaned_sentence = ''
    for char in sentence:
        if char.isalpha() or char == ' ' or char == '|':
            cleaned_sentence += char
        if char == '-':
            cleaned_sentence += ' '
    #list of stopwords 
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                 "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    #load spell checker 
    spell_checker = SpellChecker()
    #split cleaned text command into words
    sentence_lst = cleaned_sentence.split()
    num_words = len(sentence_lst)
    #placeholder for vectorized text command array
    sentence_vector = np.zeros((10, 300))
    #iterate over words in text command
    for i in range(num_words):
        word = sentence_lst[i]
        #if the word is not a stopword
        if word not in stopwords:
            #check if the vectorizer model has been trained on the word
            try:
                vectorized_word = vectorizer.wv[word]
            #if it hasn't check to see if the word is mispelled 
            except:
                misspelled = spell_checker.unknown([word])
                corrected_word = None
                for word in misspelled:
                    corrected_word = spell_checker.correction(word)
                #check to see if the spell checker was able to fix the word and the vectorizer recognizes it
                try:
                    vectorized_word = vectorizer.wv[corrected_word]
                #if not represent the token by an empty array of zeros 
                except:
                    vectorized_word = np.zeros(300)
        #if the word is a stopword, represent it by an empty array of zeros 
        else:
            vectorized_word = np.zeros(300)
        #set the corresponding index in the placeholder with the vectorized word 
        sentence_vector[i] = vectorized_word
    #dictionary object that contains vectorized text command
    numpyData = {"array": sentence_vector}
    #encode dictionary object with numpy array into json object with standard array
    output = json.dumps(numpyData, cls=NumpyArrayEncoder)
    return output


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
