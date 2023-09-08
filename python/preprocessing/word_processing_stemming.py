# -*- coding: utf-8 -*-
'''
A stemmer that operates in a word remove some
of its characters and brings it to some root form
that not necessarily has a sense.
A stemmed word does not have any affix.

Author: Fabrício Galende M. de Carvalho, PhD
'''

from nltk.stem import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import ToktokTokenizer

tokenizer = ToktokTokenizer()

porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer(language='portuguese')

sample_text_pt = ("Uma eleição muito acirrada ocorreu em 2022.",
                  "Jair Bolsonaro concorreu com Luis Inácio Lula da Silva.",
                  "Mais uma vez a democracia brasileira foi posta a prova ")
sample_text_en = ("George W Bush was a famous american president",
                  " during Irak war in the 1990's. In this period USA",
                  " bombed Irak very hard.")

sample_sentences_pt = tokenizer.tokenize_sents(sample_text_pt)
sample_stems_pt = [snowball_stemmer.stem(word) for sentence in sample_sentences_pt for word in sentence]
sample_stems_pt_2 = [porter_stemmer.stem(word) for sentence in sample_sentences_pt for word in sentence]
print("....Stemming in portuguese...")
print(sample_sentences_pt)
print(sample_stems_pt)
print(sample_stems_pt_2)


print("\n....Stemming in english....")
snowball_stemmer_2 = SnowballStemmer(language="english")
sample_sentences_en = tokenizer.tokenize_sents(sample_text_en)
sample_stems_en = [snowball_stemmer_2.stem(word) for sentence in sample_sentences_en for word in sentence]
sample_stems_en_2 = [porter_stemmer.stem(word) for sentence in sample_sentences_en for word in sentence]
print(sample_stems_en)
print(sample_stems_en_2)

