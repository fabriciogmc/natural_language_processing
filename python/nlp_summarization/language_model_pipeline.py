## This class builds a simple language model based on
## input text corpus. Text corpus is supposed
## to enter in an array of documents.

from preprocessing_pipeline import TextNormalizer
from math import log10

class BagOfWords:
    """ This class models a simple bag of words
    language model. Text corpus us supposed to enter
    in an array of documents"""
    def __init__(self, corpus, textNormalizer):
        self.corpus = corpus
        self.lexicon = None
        self.corpus_doc_size = len(corpus)
        self.corpus_sent_size = None
        self.textNormalizer = textNormalizer

    def build_doc_vector(self):
        ''' 
        Builds a array of documents. Each document is
        coposed of one or more sentences.
        '''
        doc_array = []
        for i in range(len(self.corpus)):
            sentences = self.textNormalizer.sentence_tokenizer(self.corpus[i])
            doc_array.append(sentences)
        return doc_array

    def build_model_lexicon(self):   
        ''' Creates a lexicon that corresponds to language model''' 
        doc_array = self.build_doc_vector()
        model_lexicon = {}
        document_counter = 0
        last_document = 0   
        self.corpus_sent_size = 0    
        for sentences in doc_array: #single document            
            last_sentence = 0
            sentence_counter = 0
            for sentence in sentences: #single sentence
                words = self.textNormalizer.word_tokenizer(sentence)         
                self.corpus_sent_size +=1              
                for word in words:
                    word_lower = self.textNormalizer.case_conversion(word) 
                    # stop words removal
                    if word_lower not in self.textNormalizer.stop_words:     
                        if word_lower in model_lexicon:              
                            if model_lexicon[word_lower]['last_document']!= document_counter:
                                model_lexicon[word_lower]['doc_counter'] +=1
                                model_lexicon[word_lower]['last_document'] = document_counter
                            if model_lexicon[word_lower] ['last_sentence'] != sentence_counter:
                                model_lexicon[word_lower]['sent_counter'] +=1
                                model_lexicon[word_lower] ['last_sentence'] = sentence_counter                                
                            model_lexicon[word_lower]['counter'] +=1
                        else:
                            model_lexicon[word_lower] = {'counter':1, 'doc_counter':1, 'sent_counter':1}
                            model_lexicon[word_lower]['last_document'] = document_counter
                            model_lexicon[word_lower]['last_sentence'] = last_sentence
                sentence_counter += 1
            document_counter +=1
        sorted_lexicon = dict(sorted(model_lexicon.items()))
        # removing temporary counters:
        for key in sorted_lexicon.keys():
            del model_lexicon[key]['last_document']
            del model_lexicon[key]['last_sentence']
        self.lexicon = sorted_lexicon
        return self.lexicon
    
    def build_sentence_bow(self, sentence):
        normalized_sentence = self.textNormalizer.sentence_tokenizer(sentence)
        words = self.textNormalizer.word_tokenizer(normalized_sentence[0])
        normalized_words = []        
        for word in words:
            lower_case_word = self.textNormalizer.case_conversion(word)
            if lower_case_word not in self.textNormalizer.stop_words:
                normalized_words.append(lower_case_word)
        bow_vector = []
        model_lexicon_list = list(self.lexicon)
        for position in range(len(model_lexicon_list)):
            bow_vector.append(0)
            for w in normalized_words:
                if w == model_lexicon_list[position]:
                    bow_vector[position] +=1
        return bow_vector

class TfIdfTransform:
    """ This function computes the TFIDF transform
    for some specific sentence based on some model lexicon.
    Words statistics are precalculated (sentence and document
    counters of BOW model)"""
    def __init__(self, bow_model):
        self.lang_model = bow_model

    def tfidf_transform(self, sentence):
        sentence_bow = self.lang_model.build_sentence_bow(sentence)
        tfidf_vector = []
        pos = 0
        for key in self.lang_model.lexicon:            
            tf = (1 +sentence_bow[pos])
            idf = (1+log10(self.lang_model.corpus_sent_size/(1 +self.lang_model.lexicon[key]['sent_counter'])))
            tfidf_vector.append(tf*idf)
            pos+=1
        return tfidf_vector
            
