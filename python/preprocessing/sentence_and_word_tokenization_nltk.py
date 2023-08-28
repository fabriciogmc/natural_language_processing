'''
Tokenization example.
Tokens are independent and minimal textual
components which are related to some syntax
and semantics.

Author: Fabrício Galende M. de Carvalho, DSc
Reference: Text analytics with python, Sarkar
'''
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer




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
sample_text_en = ("US unveils world's most powerful supercomputer, beats China. " 
               "The US has unveiled the world's most powerful supercomputer called 'Summit', " 
               "beating the previous record-holder China's Sunway TaihuLight. With a peak performance "
               "of 200,000 trillion calculations per second, it is over twice as fast as Sunway TaihuLight, "
               "which is capable of 93,000 trillion calculations per second. Summit has 4,608 servers, "
               "which reportedly take up the size of two tennis courts.")

basic_punctuation_marked_tokens = sample_text_pt.split(".")
print("Total basic punctuation marked tokens: ", len(basic_punctuation_marked_tokens))
print_tokens(basic_punctuation_marked_tokens)

# sent_tokenize nltk sentence tokenize
default_sentence_tokenizer = nltk.sent_tokenize


basic_sentence_tokens_en = default_sentence_tokenizer(text=sample_text_en)
basic_sentence_tokens_pt = default_sentence_tokenizer(text=sample_text_pt)
print("English:")
print("Total nltk sentece tokenizer tokens: ", len(basic_sentence_tokens_en))
print_tokens(basic_sentence_tokens_en)
print("\n\n")

print("Portuguese:")
print("Total nltk sentece tokenizer tokens: ", len(basic_sentence_tokens_pt))
print_tokens(basic_sentence_tokens_pt)
print("\n\n")

# Loading the simple Punkt Sentence Tokenizer
# C:\Users\your_user\AppData\Roaming\nltk_data\tokenizers\punkt
# This sentence tokenizer can also be used instantiating
# punkt = nltk.tokenize.PunktSentenceTokenizer()
# tokens = punkt.tokenize(text)
##
portuguese_tokenizer = nltk.data.load(resource_url='tokenizers/punkt/portuguese.pickle')
punkt_sentence_tokens_pt = portuguese_tokenizer.tokenize(sample_text_pt)
print("Total nltk punkt portuguese sentece tokenizer tokens: ", len(punkt_sentence_tokens_pt))
print_tokens(punkt_sentence_tokens_pt)
print("\n\n")

print("Now word tokenization is done:")
default_nltk_word_tokenizer = nltk.word_tokenize
words_pt = default_nltk_word_tokenizer(sample_text_pt)
print("Word portuguese tokens: ")
print(words_pt)
print("Number of tokens:", len(words_pt))

toktok_tokenizer = ToktokTokenizer()
words_toktok = toktok_tokenizer.tokenize(sample_text_pt)
print("Word portuguese tokens (toktok): ")
print(words_toktok)
print("Number of tokens:", len(words_toktok))

treebank_tokenizer = TreebankWordTokenizer()
words_treebank = treebank_tokenizer.tokenize(sample_text_pt)
print("Word portuguese tokens (treebank): ")
print(words_treebank)
print("Number of tokens:", len(words_treebank))
