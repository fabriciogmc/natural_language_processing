# Natural language processing preprocessing pipeline functions
# packed in a single class

import re


class TextNormalizer:
    """ This class perform 'all' preprocessing operations in a simplified
    document. """

    def __init__(self):
        pass

    def sentence_tokenizer(self, doc, method='punctuation'):
        """ In punctuation method, punctuation marks are used to
        mark the end of sentence. Multiple delimiters are specified
        inside [] """
        if method =='punctuation':
            sentences = re.split(r"[.?!:]", doc)
            # empty sentence removal
            non_empty_sentences = []
            for sentence in sentences:
                sentence_wo_blank = sentence.strip()      
                if sentence_wo_blank !='':
                    non_empty_sentences.append(sentence_wo_blank)
            return non_empty_sentences
        else:
            #implement your method here
            return []

    
    def word_tokenizer(self, sentence):
        """Split sentence in word tokens using blank spaces, semicolon and 
        comma. Input is a sentence string without end punctuation. """
        words = re.split(r"[,;\s]", sentence)
        non_empty_words = []
        for word in words:
            if word !="":
                non_empty_words.append(word)
        return non_empty_words   
    
    def case_conversion(self, word, method='lower'):
        if method == 'lower':
            return word.lower()
        if method == 'upper':
            return word.upper()
        


class TfIdfTransform:
    def __init__(self, reference_corpora):
        pass
    def tfidf_transform(self, doc):
        pass

class ExtractiveSummarizer:
    def __init__(self, reference_corpora):
        pass

    def document_score(self):
        pass

    def build_rank(self, docs):
        pass

    def build_summary(self, docs):

        pass
    
    
