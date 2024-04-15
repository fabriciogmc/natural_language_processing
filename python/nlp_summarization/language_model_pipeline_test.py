from preprocessing_pipeline import TextNormalizer
from language_model_pipeline import BagOfWords, TfIdfTransform


my_docs = ["Adorei o produto! O Produto é muito bom.", "Produto mediano"]
my_text_normalizer = TextNormalizer()
my_bow = BagOfWords(my_docs, my_text_normalizer)

my_doc_vector = my_bow.build_doc_vector()
print("Array of documents transformed to array of sentences. ")
print(my_doc_vector)

# Creating a model lexicon
my_model_lexicon = my_bow.build_model_lexicon()
print("Model lexicon: ")
print(my_model_lexicon)

# Evaluating the model for a specific sentence
my_sentence = "adorei o bom produto, produto muito mediano "
my_sentence_bow = my_bow.build_sentence_bow(my_sentence)
print("Corresponding sentence bow vector: ")
print(my_sentence_bow)

#Exemplifying TFIDF transform
my_tfidf = TfIdfTransform(my_bow)
tf_idf_vector = my_tfidf.tfidf_transform(my_sentence)
print("TFIDF vector representing the sentence:")
print(tf_idf_vector)

