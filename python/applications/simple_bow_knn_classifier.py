'''
In this example it is shown a simplest form of sentence knn
classification.

Author: Fabrício Galende M. de Carvalho, DSc
'''

import numpy as np

classified_reviews= [
    {'corpus': "adorei o produto", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "detestei o produto ", 'review_type': 'negative', 'feature_vector': []},
    {'corpus': "produto satisfatório", 'review_type': 'neutral', 'feature_vector': []}    
]
unclassified_review = {
    'corpus': 'adorei muito esse produto',
    'review_type': '',
    'feature_vector': []
}

base_model_lexicon = ['a', 'ajuda', 'ajudar', 'confusão', 'bom', 'mau', 
                 'atendimento', 'como', 'confuso', 
                 'consigo', 'de', 'desejo', 'encerrar', 
                 'estou', 'favor', 'gostaria', 'há', 'mais',
                   'me', 'não', 'obter', 'opção', 'outra', 'poderia', 
                   'por', 'qual', 'sei', 'é', 'essa']

# words used as inputs shall be those resulted from tokenization proccess and other
# preprocessing steps.
def build_model_lexicon(words, model_lexicon):
    for word in words:
        if word not in model_lexicon:
            model_lexicon.append(word)
    model_lexicon.sort()

def build_feature_vector(words, model_lexicon):
    bag_of_words_count = np.zeros(len(model_lexicon))
    for pos in range(len(model_lexicon)):
        for word in words:
            if word == model_lexicon[pos]:
                bag_of_words_count[pos] += 1
    return bag_of_words_count


# Here we build the model lexicon
for classified_review in classified_reviews:
    build_model_lexicon(classified_review['corpus'].split(), base_model_lexicon)
build_model_lexicon(unclassified_review['corpus'].split(), base_model_lexicon)

# Now we extract the feature vector considering the model
for classified_review in classified_reviews:
    classified_review['feature_vector'] = build_feature_vector(classified_review['corpus'].split(), base_model_lexicon)

unclassified_review['feature_vector'] = build_feature_vector(unclassified_review['corpus'].split(), base_model_lexicon)

# Now we perform the classification:
dot_product_values = []
for classified_review in classified_reviews:
    dot_product_values.append({"class":classified_review['review_type'], 
                               "score": np.dot(unclassified_review['feature_vector'], classified_review['feature_vector'])})
dot_product_sorted = sorted(dot_product_values, key=lambda d: d['score'], reverse=True)
print(dot_product_sorted)
unclassified_review['review_type'] = dot_product_sorted[0]['class']
print("Review classified as: ", unclassified_review['review_type'])



