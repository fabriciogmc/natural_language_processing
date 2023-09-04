# -*- coding: utf-8 -*-
'''
This example shows a simple spell check based
upon library usage

Author: Fabrício Galende M. de Carvalho, DSc

Reference: https://pyspellchecker.readthedocs.io/en/latest/
'''

from spellchecker import SpellChecker
portuguese = SpellChecker(language='pt')  
misspelled_word = "abacachi"
corrected_word = portuguese.correction(misspelled_word)
print(corrected_word)