'''
In this code, document similarity categorization is performed.
TFIDF document model is used before similarity computation is
performed.

Author: Fabricio Galende M. de Carvalho, DSc
'''

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import linkage, fcluster
from pandas import DataFrame
import pandas as pd

documents = ["hoje faz muito calor",
             "hoje está frio e a temperatura caiu",
             "a temperatura está alta e faz calor",
             "a comida desse restaurante é ótima",
             "os pratos do restaurante são ótimos",
             "adoramos todos os pratos",
             "a temperatura está baixa e faz frio"]
#Building text corpus dataframe to visualize document clusters
corpus_df = DataFrame({"Document": documents})
tfidf_vectorized = TfidfVectorizer(min_df=0., max_df=1., norm='l2', use_idf=True)
features = tfidf_vectorized.fit_transform(documents)
model_lexicon = tfidf_vectorized.get_feature_names_out()
feature_vectors = features.toarray()
print(model_lexicon)
print(feature_vectors)
print("Vectorized corpus document models: ")
feature_df = DataFrame(feature_vectors,columns= model_lexicon).transpose()
print(feature_df)

# Similarity matrix computation
similarity_matrix = cosine_similarity(feature_vectors)
Z = linkage(similarity_matrix, 'ward')
max_dist = 2.
cluster_labels = fcluster(Z, max_dist, criterion='distance')
cluster_labels = DataFrame(cluster_labels, columns=['Cluster Label'])
final_table = pd.concat([corpus_df, cluster_labels], axis=1)
print(final_table)
