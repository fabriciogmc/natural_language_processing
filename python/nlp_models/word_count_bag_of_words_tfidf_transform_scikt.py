'''
This code exemplifies bag of words model using
scikit-learn python library with term frequency times
inverse document frequency transform.

Author: Fabricio Galende M. de Carvalho, DSc
'''

from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import DataFrame

documents = ["gostei do computador",
             "não gostei do computador"]
tfidf_vectorized = TfidfVectorizer(min_df=0., max_df=1., norm='l2', use_idf=True)
features = tfidf_vectorized.fit_transform(documents)
model_lexicon = tfidf_vectorized.get_feature_names_out()
feature_vectors = features.toarray()
print(model_lexicon)
print(feature_vectors)
print("Vectorized corpus document models: ")
feature_df = DataFrame(feature_vectors,columns= model_lexicon).transpose()
print(feature_df)


#performing new document count vectorization based upon the model already built
new_doc = ["não gostei"]
feature_vector = tfidf_vectorized.transform(new_doc).toarray()
feature_df_new_model = DataFrame(feature_vector, columns = model_lexicon).transpose()
print("new input document model")
print(feature_df_new_model)

