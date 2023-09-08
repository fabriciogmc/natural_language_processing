# Creating a bag of words model which only verify if some word
# occurs in model lexicon
# Typically model lexicon is obtained from text  corpora.
#
# Author: Fabrício Galende M. de Carvalho, DSc
##



model_lexicon = ['a', 'ajuda', 'ajudar', 'confusão', 'bom', 'mau', 
                 'atendimento', 'como', 'confuso', 
                 'consigo', 'de', 'desejo', 'encerrar', 
                 'estou', 'favor', 'gostaria', 'há', 'mais',
                   'me', 'não', 'obter', 'opção', 'outra', 'poderia', 
                   'por', 'qual', 'sei']
model_lexicon.sort()
print(model_lexicon)

sentence = "gostaria de obter ajuda" # raw sentence example, without any preprocessing
words = sentence.split() ## replace by some tokenizer output

bag_of_words = []
for w in model_lexicon:
    if w in words:
        bag_of_words.append(1)
    else:
        bag_of_words.append(0)
print(bag_of_words)



