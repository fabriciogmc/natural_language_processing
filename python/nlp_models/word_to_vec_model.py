'''
This file exemplifies a simple word2vec
model. This model was proposed by Google
an try to approximate each word by a
'continuous' dense vector. In theory, similar
words will have similar vectors.
In this example the gensim library will be used

Author: Fabrício Galende M. de Carvalho, DSc
'''
import re
import numpy as np
from numpy import dot 
from numpy.linalg import norm
from numpy import average
from numpy import vectorize
from gensim.models import word2vec
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

text_corpus = "Os melhores produtos " \
"são vendidos por uma loja que se preocupa "\
"com a experiência do cliente. Muitos adoram " \
"produtos que chegam no prazo ou que satisfazem "\
"suas expectativas. Pessoas não gostam de produtos "\
"vendidos com tamanhos incorretos, inadequados "\
"ou que chegam em atraso. Pessoas também amam produtos "\
"que atendem a todas as suas expectativas. "



print(text_corpus)
tokenizer = sent_tokenize
# 1. Basic sentence tokens building
sentence_tokens = tokenizer(text_corpus)
print("Sentence tokens: ")
print(sentence_tokens)
print("\n\n")
# 2. Basic word tokens building
word_tokens = [ word_tokenize(sentence)  for sentence in sentence_tokens]
print("Word tokens: ")
print(word_tokens)
print("\n\n")

# 3. Removing punctuation characters and converting
# all charecters to lower case:
normalized_sentences = []
i = 0
for sentence in word_tokens:
    normalized_sentences.append([])
    for word in sentence:
        word = re.sub(r'[^A-Za-zÀ-Ýà-ý]','', word).lower()
        if word!='':
            normalized_sentences[i].append(word)
    i = i+1

print("\n\n")
print("Lower case, punctuation free word tokens")
print(normalized_sentences)

# 4. Stop word removal:
stop_words = ['a', 'as', 'e', 'o', 'os', 'da', 'de', 'do', 'um', 'uma']
for word in stop_words:
    for sentence in normalized_sentences:
        if word in sentence:
            print(word)
            print(sentence)
            sentence.remove(word)
print("\n\n")
print("Normalized text: ")
print(normalized_sentences)

# 4. building the word2vec model
# Model configuration
feature_size = 5  # size of vector representation
window_context = 2
min_word_count = 1
sample = 1e-3
w2vec_model = word2vec.Word2Vec(normalized_sentences, vector_size= feature_size,
                                window=window_context, min_count= min_word_count,
                                sample=sample, epochs = 50)


v1 = w2vec_model.wv["adoram"]
v2 = w2vec_model.wv["amam"]
v3 = w2vec_model.wv["atraso"]
print(v1)
print(v2)
print(v3)
print("Cosine similarity between 'adoram' and 'amam': ")
print(dot(v1,v2)/(norm(v1)*norm(v2)))

print("Cosine similarity between 'amam' and 'atraso': ")
print(dot(v1,v3)/(norm(v1)*norm(v3)))

# Now we model a single document that must have words present
# in original corpus used to train the model. This document models,
# for example, a single product review, etc.

doc = "pessoas adoram os produtos"
normalized_doc = doc.split()
normalized_doc.remove('os')
print(normalized_doc)
word_embedding = [] 
for word in normalized_doc:
    word_embedding.append(w2vec_model.wv[word])
word_embedding = np.array(word_embedding)
print("\n \n")
print("Document word embeddings: ")
print(word_embedding)

doc_embedding = np.zeros(feature_size)
print(doc_embedding)
for i in range(len(doc_embedding)):     
    doc_embedding[i] = average(word_embedding[:,i])
print("\n \n")
print("Document feature vector based upon word embeddings: ")
print(doc_embedding)





                               
