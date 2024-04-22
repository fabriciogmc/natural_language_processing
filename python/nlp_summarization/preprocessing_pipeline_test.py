##
# Calling preprocesing pipiline functions:
#
# Fabrício G. M. de Carvalho, D.Sc.
##

from preprocessing_pipeline import TextNormalizer

my_doc = "Esse produto é      muito, bom! Adorei! Que legal!"
stop_words = ['que', 'esse', 'aquele']
my_normalizer = TextNormalizer(stop_words)

print("Original document: ", my_doc)

# lower case conversion
my_doc_lower = my_normalizer.case_conversion(my_doc)
print("Document in lower case: ", my_doc_lower)

# Sentence tokenization 
sentence_tokens = my_normalizer.sentence_tokenizer(my_doc_lower)
print("Document sentence tokens: ", sentence_tokens)

# word tokenization
words = my_normalizer.word_tokenizer(sentence_tokens[0])
print("Words that copose document:", words)

# stop words removal:
words_without_stop_words = my_normalizer.stop_words_removal(words)
print("Document words without stop words: ",  words_without_stop_words)
