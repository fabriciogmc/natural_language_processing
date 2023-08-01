import spacy
from spacy import displacy
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
pos_tags_2 = [ (word, word.tag_,  word.pos_) for word in nlp(sentence)]
pos_tags_2_df = pd.DataFrame(pos_tags_2).T
print(pos_tags_2)
print(pos_tags_2_df)

print("Building dependency grammar:")
#displacy.render(nlp(sentence), jupyter=True, 
#         options={'distance':100, 'arrow_stroke': 1.5, 'arrow_width':8})
displacy.serve(nlp(sentence), options={'distance':100, 'arrow_stroke': 1.5, 'arrow_width':8})



