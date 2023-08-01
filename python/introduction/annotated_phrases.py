import nltk
import spacy
import numpy as np
import pandas as pd
import copy as cp

sentence = "Donald Trump was the USA president in 2020"
words = sentence.split()
bag_of_words = cp.deepcopy(words)
np.random.shuffle(bag_of_words)
# Bag of words:
print(bag_of_words)

# Annotated words:
print("Using spacy to get parts of speech tags.")
nlp = spacy.load('en_core_web_sm')
pos_tags = [ (word, word.tag_,  word.pos_) for word in nlp(sentence)]
pos_tags_df = pd.DataFrame(pos_tags).T
print(pos_tags)
print(pos_tags_df)

grammar = '''
    NP: {<DT>?<JJ>?<NN.*>}
    ADJP: {<JJ>}
    ADVP: {<RB.*>}
    PP: {<IN>}
    VP: {<MD>?<VB.*>+}
'''
rp = nltk.RegexpParser(grammar)
shallow_parsed  = rp.parse(pos_tags)
for x in shallow_parsed:
    i = 0
    for j in x:
        print(i)        
        print(j)





