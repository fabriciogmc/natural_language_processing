# -*- coding: utf-8 -*-
'''
Processing specific words to remove or replace special
characters

Author: Fabrício Galende M. de Carvalho, DSc
Reference: Text analytics with python, Sarkar
'''
import nltk
import unicodedata
import re
from nltk.corpus import mac_morpho
from textblob import Word


# Here we remove accented characters if we want.
def remove_accents(text):
    ''' This function removes accented characters. '''
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

# Here you define your contraction, abbreviation and other similar
# maps.
MAP = {
    'LTDA': 'limitada',
    'nda': 'nada',
    "d'água": 'de água' 
}

def expand_abbreviations_and_contractions(text, contraction_mapping):
    ''' 
    This function expands contractions, abbreviations, etc
    '''
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())                       
        expanded_contraction = first_char+expanded_contraction[1:]
        return expanded_contraction
        
    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text


# We can correct spelling errors by looking at some
# text corpora. In this example we can replace repeated
# characters that occurs in misspelled words. The text corpora
# that has been used was MacMorpho

def remove_repeated_characters(token):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if old_word in mac_morpho.words():
            print('here...')
            return old_word
        print("There")
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word
            
    correct_tokens = replace(token)
    return correct_tokens


####################################


sample_text = ("Ele é um bom estudante. "
               "Trabalha na empresa optimum LTDA. "
                "Adora beber um copo d'água quando acorda.")
sample_text_wo_accents = remove_accents(sample_text)
word_tokenizer = nltk.ToktokTokenizer()
sample_words = word_tokenizer.tokenize(sample_text_wo_accents)
print(sample_words)
sample_text_wo_abbr_and_contr = expand_abbreviations_and_contractions(sample_text,MAP)
print("Expanded text: ")
print(sample_text_wo_abbr_and_contr)

## Correcting spelling errors (repetition):
word = "friiio"
#corrected_word = remove_repeated_characters(word)
#print(corrected_word)

