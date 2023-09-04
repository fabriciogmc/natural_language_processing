# -*- coding: utf-8 -*-
'''
This example shows a simple spell check based
upon distance calculation.

Author: Fabrício Galende M. de Carvalho, DSc
Reference: Text analytics with python, Sarkar
'''
import re
from nltk.corpus import mac_morpho


import re, collections

def tokens(text): 
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower()) 

# attention: not all tokens that are joined shall
# be considered as correct words. This is a simple
# didactic example. 

WORDS = tokens(' '.join(mac_morpho.words()))
WORD_COUNTS = collections.Counter(WORDS)
# top 20 words in corpus
print(WORD_COUNTS.most_common(20))

def edits0(word): ## Sarkar
    """
    Return all strings that are zero edits away 
    from the input word (i.e., the word itself).
    """
    return {word}



def edits1(word): ## Sarkar
    """
    Return all strings that are one edit away 
    from the input word.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    def splits(word):
        """
        Return a list of all possible (first, rest) pairs 
        that the input word is made of.
        """
        return [(word[:i], word[i:]) 
                for i in range(len(word)+1)]
                
    pairs      = splits(word)
    deletes    = [a+b[1:]           for (a, b) in pairs if b]
    transposes = [a+b[1]+b[0]+b[2:] for (a, b) in pairs if len(b) > 1]
    replaces   = [a+c+b[1:]         for (a, b) in pairs for c in alphabet if b]
    inserts    = [a+c+b             for (a, b) in pairs for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known(words): ## Sarkar
    """
    Return the subset of words that are actually 
    in our WORD_COUNTS dictionary.
    """
    return {w for w in words if w in WORD_COUNTS}

def correct(word): #Sarkar
    """
    Get the best correct spelling for the input word
    """
    # Priority is for edit distance 0, then 1, then 2
    # else defaults to the input word itself.
    candidates = (known(edits0(word)) or 
                  known(edits1(word)) or                   
                  [word])
    return max(candidates, key=WORD_COUNTS.get)

misspelled_word = 'pota'

# verifying the 1-edit distance word set:
print("Generating 1-edit distance words from the original misspelled word: ")
print(edits1(misspelled_word))
print("-------------------")

print("Verifying which belong to text corpus. ")
print(known(edits1(misspelled_word)))

print("Selecting one which is most likely right")

print(correct(misspelled_word))




