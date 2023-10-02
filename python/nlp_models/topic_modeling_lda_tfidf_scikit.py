'''
A simple topic modeling example.

Author: Fabricio Galende M. de Carvalho, DSc
'''

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from pandas import DataFrame

documents = ["gostamos muito de comida realmente uma comida deliciosa",
             "a comida não estava boa pois o gosto não agradou",
             "o vestido estava muito apertado e não coube",
             "o vestido está na medida certa e coube bem",
             "algo que gera muitas duvidas para todos"]
tfidf_vectorized = TfidfVectorizer(min_df=0., max_df=1., norm='l2', use_idf=True)
features = tfidf_vectorized.fit_transform(documents)
model_lexicon = tfidf_vectorized.get_feature_names_out()
feature_vectors = features.toarray()
lda = LatentDirichletAllocation(n_components=3, max_iter=10000, random_state=0)
dt_matrix = lda.fit_transform(feature_vectors)
topic_features = DataFrame(dt_matrix, columns=["topic 1", "topic 2", "topic 3"])
print(topic_features)
vocab = model_lexicon
topic_matrix = lda.components_
tt_matrix = lda.components_
for topic_weights in tt_matrix:
    topic = [(token, weight) for token, weight in zip(vocab, topic_weights)]
    topic = sorted(topic, key=lambda x: -x[1])
    topic = [item for item in topic if item[1] > 0.6]
    print(topic)
    print()

     


