# Examples of text preprocessing using some famous text corpus

from nltk.corpus import gutenberg
from nltk.corpus import stopwords
# from nltk.corpus import mac_morpho
import matplotlib.pyplot as plt
from collections import Counter
import re

# Remark, in windows, text copus data can tipically be found at
# Users\<your_user_name>\AppData\Roaming\nltk_data\corpora\<corpora_name>
bible = gutenberg.open('bible-kjv.txt')
bible = bible.readlines()
print(bible[:5])

# Removing newline characters
bible_wo_nl = [line.strip('\n') for line in bible]
print(bible_wo_nl[:5]) 

# Removing lines without any character
bible_wo_el = list(filter(None, bible_wo_nl))
print(bible_wo_el[:5])

# Accesing the iterable returned by the filter
x=0
for item in filter(None, bible_wo_nl):
    print("Line #", x)
    print(item)
    x = x +1
    if x > 10:
        break

# Performing some frequency analysis with respect to line lengths
line_lengths = [len(sentence) for sentence in bible_wo_el]
h = plt.hist(line_lengths)
plt.title("Computing the character length of each sentence.")
plt.xlabel("sentence length")
plt.ylabel("sentence count")
plt.show()

line_tokens = [sentence.split() for sentence in bible_wo_el]
print(line_tokens[:5])
tokens_count = [len(token_sentence) for token_sentence in line_tokens]
h_t = plt.hist(tokens_count, color='red')
plt.title("Computing the word length of each sentence")
plt.xlabel("tokens per line")
plt.ylabel("line count")
plt.show()


# flattening the list to compute the most common words
# remark: mutilist comprehension [ outer loop ... inner loop]
words =[ word for token_sentence in line_tokens for word in token_sentence]
print(words[:20])

# Removing symbols and special characters
words_clean = [ re.sub(r'[^A-Za-z]','', word).lower() for word in words]
# Removing empty characters
words_clean = list(filter(None, words_clean))
print(words_clean[:30])

# Counting word frequency
c = Counter(words_clean)
print("Most common words in text corpus:")
print(c.most_common(10))

# removing stopwords
stop_words = stopwords.words('english')
words_clean_wo_sw = [ word_clean for word_clean in words_clean if word_clean not in stop_words]
c_wo_sw = Counter(words_clean_wo_sw)
print("Word counts without stopwords:")
print(c_wo_sw.most_common(10))


'''
sentences = mac_morpho.sents()
sentencas_marcadas = mac_morpho.tagged_sents()
print(sentencas_marcadas[:5])
for sentencas in sentencas_marcadas[:5]:
    frase = ' '
    for palavras_marcadas in sentencas:
        frase = frase + ' ' + palavras_marcadas[0]
    print(frase)
'''



