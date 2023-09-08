'''
Stop words are words that do not aggregate too much meaning
in text. These words are very frequent in text corpus.
Examples include articles, prepositions, etc.

Author: Fabrício Galende M. de Carvalho, DSc

'''
import nltk
from nltk.tokenize.toktok import ToktokTokenizer






def print_tokens(tk):
    tc = 1
    print('Total tokens: ', len(tk))
    for token in tk:
        print("Token #", tc, ":", token)
        tc += 1

sample_text_pt = """
Hoje de manhã Pedro acordou com muita fome. Levantou,
escovou os dentes, lavou o rosto e foi para a cozinha.
Abriu a geladeira, pegou uma jarra de suco e três ovos.
Tomou um copo d'água. Fritou os ovos. Sentou na mesa e saboreou seu café da 
manhã...
"""

sample_text_pt_positive = "eu gostei do computador"
sample_text_pt_negative = "eu não gostei do computador"

sample_text_en = ("US unveils world's most powerful supercomputer, beats China. " 
               "The US has unveiled the world's most powerful supercomputer called 'Summit', " 
               "beating the previous record-holder China's Sunway TaihuLight. With a peak performance "
               "of 200,000 trillion calculations per second, it is over twice as fast as Sunway TaihuLight, "
               "which is capable of 93,000 trillion calculations per second. Summit has 4,608 servers, "
               "which reportedly take up the size of two tennis courts.")

# sent_tokenize nltk sentence tokenize
default_sentence_tokenizer = nltk.sent_tokenize
basic_sentence_tokens_pt = default_sentence_tokenizer(text=sample_text_pt)

print("Portuguese:")
print("Total nltk sentece tokenizer tokens: ", len(basic_sentence_tokens_pt))
print_tokens(basic_sentence_tokens_pt)
print("\n\n")
print("Now word tokenization is done:")
default_nltk_word_tokenizer = nltk.word_tokenize
words_pt = default_nltk_word_tokenizer(sample_text_pt)
("\n\n***********")
print("Portuguese word tokens: ")
print(words_pt)
print("Number of tokens before stop words removal:", len(words_pt))

#print("Stop word list: ")
print(nltk.corpus.stopwords.words('portuguese'))

def remove_stopwords(text_tokens, stopwords):
    for word in text_tokens:
        if word in stopwords:
            text_tokens.remove(word)

remove_stopwords(words_pt, nltk.corpus.stopwords.words('portuguese'))
print("\n\n***********")
print("Portuguese word tokens (after stop words removal):")
print(words_pt)
print("Number of tokens after stop words removal:", len(words_pt))
print("\n\n\n")
print("Preserving sentece meaning after stopword removal: ")
words_pt = default_nltk_word_tokenizer(sample_text_pt_positive)
remove_stopwords(words_pt, nltk.corpus.stopwords.words('portuguese'))
print(words_pt)
words_pt = default_nltk_word_tokenizer(sample_text_pt_negative)
remove_stopwords(words_pt, nltk.corpus.stopwords.words('portuguese'))
print(words_pt)





