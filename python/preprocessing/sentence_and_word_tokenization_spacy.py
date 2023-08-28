# -*- coding: utf-8 -*-
'''
Tokenization example.
Tokens are independent and minimal textual
components which are related to some syntax
and semantics.
Instead of using nltk, this file uses Spacy tokenizer.

Author: Fabrício Galende M. de Carvalho, DSc
Reference: Text analytics with python, Sarkar
'''
import spacy



def print_tokens(tk):
    tc = 1
    print('Total tokens: ', len(tk))
    for token in tk:
        print("Token #", tc, ":", token)
        tc += 1

sample_text_pt = """
Hoje de manhã Pedro acordou com muita fome! Levantou,
escovou os dentes, lavou o rosto e foi para a cozinha.
Abriu a geladeira, pegou uma jarra de suco e três ovos.
Tomou um copo d'água. Fritou os ovos. Sentou na mesa e saboreou seu café da 
manhã...
"""
sample_text_en = ("US unveils world's most powerful supercomputer, beats China. " 
               "The US has unveiled the world's most powerful supercomputer called 'Summit', " 
               "beating the previous record-holder China's Sunway TaihuLight. With a peak performance "
               "of 200,000 trillion calculations per second, it is over twice as fast as Sunway TaihuLight, "
               "which is capable of 93,000 trillion calculations per second. Summit has 4,608 servers, "
               "which reportedly take up the size of two tennis courts.")

model_spacy = spacy.load('pt_core_news_sm')
basic_word_tokens_pt = model_spacy(sample_text_pt)
sentences = [ sent for sent in basic_word_tokens_pt.sents]
basic_sentence_tokens_pt = sentences
print("Sentece tokens, portuguese spacy tokenizer default: ")
print_tokens(basic_sentence_tokens_pt)
print("Number of tokens: ", len(basic_sentence_tokens_pt))
print("Work tokens, portuguese, spacy tokenizer default: ")
basic_word_tokens_pt = list(basic_word_tokens_pt)
print(basic_word_tokens_pt)
print("Number of tokens: ", len(basic_word_tokens_pt))
print("Second word token: ", basic_word_tokens_pt[1]);




