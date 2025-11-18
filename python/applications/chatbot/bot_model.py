import re
import pickle
import numpy as np
from nltk.tokenize import word_tokenize
from gensim.models import word2vec


word2vec_model_loaded = word2vec.Word2Vec.load("word2vec_bot.model")
with open("mlp_classifier.pkl", "rb") as f:
    loaded_classifier = pickle.load(f)

def preprocess(text_input):
    user_input_word_tokens = word_tokenize(text_input)
    user_input_normalized_word_tokens = []
    for word in user_input_word_tokens:
        word = re.sub(r'[^A-Za-zÀ-Ýà-ý]','', word).lower()
        if word!='':
            user_input_normalized_word_tokens.append(word)
    return user_input_normalized_word_tokens

def representation(user_input_normalized_word_tokens):
    input_sentence_vector = np.zeros(word2vec_model_loaded.vector_size)
    nwords = 0
    for word in user_input_normalized_word_tokens:
        if word in word2vec_model_loaded.wv:
            nwords +=1
            input_sentence_vector += word2vec_model_loaded.wv[word]
    input_sentence_vector /= nwords
    return input_sentence_vector

def classify(input_sentence_vector):
    predicted_class = loaded_classifier.predict(input_sentence_vector.reshape(1, -1))
    return str(predicted_class)