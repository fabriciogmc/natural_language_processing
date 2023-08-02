# Creating a bag of words model:
# Typically model lexicon is obtained from text  corpora.

model_lexicon = ['a', 'ajuda', 'ajudar', 
                 'atendimento', 'como', 'confuso', 
                 'consigo', 'de', 'desejo', 'encerrar', 
                 'estou', 'favor', 'gostaria', 'há', 'mais',
                   'me', 'não', 'obter', 'opção', 'outra', 'poderia', 
                   'por', 'qual', 'sei']
sentence = "gostaria de obter ajuda"
words = sentence.split()
bag_of_words = []
for w in model_lexicon:
    if w in words:
        bag_of_words.append(1)
    else:
        bag_of_words.append(0)
print(bag_of_words)

