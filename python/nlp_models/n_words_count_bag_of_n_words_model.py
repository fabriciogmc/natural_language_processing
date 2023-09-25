'''
A simple bag of n-words model.

Author: Fabrício Galende M. de Carvalho, DSc
'''
import nltk
from nltk.util import ngrams
default_nltk_word_tokenizer = nltk.word_tokenize



reference_text_corpus = [
    "adorei muito esse produto",
    "não gostei nada desse produto",
]
review = "adorei muito produto mais que os demais"


def build_model_lexicon(text_corpus_list):
    model_lexicon = []
    for sentence in text_corpus_list:
        words = default_nltk_word_tokenizer(sentence)
        ngrams_2 = list(ngrams(words,2))
        for ngram_ in ngrams_2:
            if ngram_ not in model_lexicon:
                model_lexicon.append(ngram_)
    return model_lexicon

def build_feature_vector(text, model_lexicon): 
    words = default_nltk_word_tokenizer(text)
    ngrams_2_text = list(ngrams(words,2))
    feature_vector = []
    for ngrams_2_model in model_lexicon:
        if ngrams_2_model in ngrams_2_text:
            feature_vector.append(1)
        else:
            feature_vector.append(0)
    return feature_vector

model = build_model_lexicon(reference_text_corpus)
print(model)

feature_ref_1 = build_feature_vector(reference_text_corpus[0], model)
feature_ref_2 = build_feature_vector(reference_text_corpus[1], model)
feature_review = build_feature_vector(review, model)

print("Feature vectors for corpus and review: ")
print("reference text 1: ")
print(feature_ref_1)
print("reference text 2: ")
print(feature_ref_2)
print("reference review: ")
print(feature_review)

