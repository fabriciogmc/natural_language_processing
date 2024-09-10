'''
This example illustrates word lemmatization.
While stems do not necessarily have a sense (stem root)
a lemma will always have a sense (word root). I both
cases affixes are removed from the original word.

Author Fabrício Galende M. de Carvalho, PhD
'''
import spacy
from nltk.tokenize import word_tokenize
import stanza

# stanza.download('pt')
stanza_nlp = stanza.Pipeline('pt')


sample_text_pt = "Nesse mês ocorreu um fenômeno muito raro durante a primeira semana."
sample_text_pt_2 = (" a mulherada correu e viu a lindíssima floreira no vaso da janela" 
                     " rapidamente notou-se que precisaria de água" 
                     " a puríssima e a riquíssima responsável pela vida ")

spacy_nlp = spacy.load('pt_core_news_sm',  disable = ['parser','ner'])
print([ token.lemma_ for token in spacy_nlp(sample_text_pt)])
print([ word.lemma for sentence in stanza_nlp(sample_text_pt).sentences for word in sentence.words])

print([ token.lemma_ for token in spacy_nlp(sample_text_pt_2)])
print([ word.lemma for sentence in stanza_nlp(sample_text_pt_2).sentences for word in sentence.words])





