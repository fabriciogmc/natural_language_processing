'''
A pairwise consine similarity model example

Author: Fabrício Galende M. de Carvalho, DSc
'''

import numpy as np
import pandas as pd
model_lexicon = []

sentences = ["gostaria de obter ajuda e essa ajuda é importante",
             "acho que vai chover e está nublado",
             "não acho que vai chover hoje pois faz sol",
             "como será que posso obter ajuda",
             "não consigo obter ajuda de jeito nenhum"]

def build_model_lexicon(sentences, model_lexicon):
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word not in model_lexicon:
                model_lexicon.append(word)

def build_feature_vector(sentence, model_lexicon):
    feature_vector = np.zeros(len(model_lexicon))
    for pos in range(len(model_lexicon)):
        for word_s in sentence.split():
            if word_s == model_lexicon[pos]:
                feature_vector[pos] +=1
    return feature_vector

build_model_lexicon(sentences, model_lexicon)
feature_vectors=[]
for s in sentences:
    feature_vectors.append(build_feature_vector(s,model_lexicon))

similarity_matrix = []
for x in range(len(feature_vectors)):
    similarity_matrix.append([])
    for y in range(len(feature_vectors)):
        similarity_matrix[x].append( np.dot(feature_vectors[x],
                                            feature_vectors[y])/ (np.linalg.norm(feature_vectors[x])*np.linalg.norm(feature_vectors[y]) ))

for line in similarity_matrix:
    print(line)


