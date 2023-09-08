'''
In this model, word occurrence frequency is used
to build the bag of words model.

Author: Fabrício Galende M. de Carvalho, DSc
'''

import numpy as np
import pandas as pd
model_lexicon = ['a', 'ajuda', 'ajudar', 'confusão', 'bom', 'mau', 
                 'atendimento', 'como', 'confuso', 
                 'consigo', 'de', 'desejo', 'encerrar', 
                 'estou', 'favor', 'gostaria', 'há', 'mais',
                   'me', 'não', 'obter', 'opção', 'outra', 'poderia', 
                   'por', 'qual', 'sei', 'é', 'essa']

sentence = "gostaria de obter ajuda e essa ajuda é importante" # raw sentence example, without any preprocessing
words = sentence.split() ## replace by some tokenizer output

bag_of_words_count = np.zeros(len(model_lexicon))

for pos in range(len(model_lexicon)):
    for word in words:
        if word == model_lexicon[pos]:
            bag_of_words_count[pos] += 1

model_data_frame = pd.DataFrame(model_lexicon, bag_of_words_count)
#print(bag_of_words_count)
print(model_data_frame)