import numpy as np
from gensim import models
import gensim.downloader as api
from spellchecker import SpellChecker
import json
from json import JSONEncoder
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


vectorizer = models.KeyedVectors.load_word2vec_format(
    "./data/google-word2vec.bin", binary=True)


@app.route('/', methods=['POST'])
@cross_origin()
def home():
    data = request.get_json()
    sentence = data['command']
    cleaned_sentence = ''
    for char in sentence:
        if char.isalpha() or char == ' ':
            cleaned_sentence += char
        if char == '-':
            cleaned_sentence += ' '
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                 "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    spell_checker = SpellChecker()
    sentence_lst = cleaned_sentence.split()
    num_words = len(sentence_lst)
    sentence_vector = np.zeros((10, 300))
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
    for j in range(num_words, 10, 1):
        sentence_vector[j] = np.zeros(300)
    numpyData = {"array": sentence_vector}
    output = json.dumps(numpyData, cls=NumpyArrayEncoder)
    return output


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
