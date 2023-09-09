'''
This code exemplifies bag of words model using
scikit-learn python library.

Author: Fabricio Galende M. de Carvalho, DSc
'''

from sklearn.feature_extraction.text import CountVectorizer
from pandas import DataFrame

documents = ["gostei do computador",
             "não gostei do computador"]
counter_vectorize = CountVectorizer(min_df=0., max_df= 1.)
features = counter_vectorize.fit_transform(documents)
model_lexicon = counter_vectorize.get_feature_names_out()
feature_vectors = features.toarray()
print(model_lexicon)
print(feature_vectors)
print("Vectorized corpus document models: ")
feature_df = DataFrame(feature_vectors,columns= model_lexicon).transpose()
print(feature_df)


#performing new document count vectorization based upon the model already built
new_doc = ["não gostei"]
feature_vector = counter_vectorize.transform(new_doc).toarray()
feature_df_new_model = DataFrame(feature_vector, columns = model_lexicon).transpose()
print("new input document model")
print(feature_df_new_model)

