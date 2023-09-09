from sklearn.neural_network import MLPClassifier
import numpy as np

classified_reviews= [
    {'corpus': "adorei o produto", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "amei o produto ", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "achei o produto excelente", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "com certeza comprarei novamente ", 'review_type': 'positive', 'feature_vector': []},
    {'corpus': "detestei o produto ", 'review_type': 'negative', 'feature_vector': []}, 
    {'corpus': "produto horrível ", 'review_type': 'negative', 'feature_vector': []}, 
    {'corpus': "nunca mais compro novamente ", 'review_type': 'negative', 'feature_vector': []},  
    {'corpus': "pior produto que comprei ", 'review_type': 'negative', 'feature_vector': []},    
    {'corpus': "produto satisfatório", 'review_type': 'neutral', 'feature_vector': []},
    {'corpus': "produto atende as necessidades", 'review_type': 'neutral', 'feature_vector': []},   
    {'corpus': "produto ok", 'review_type': 'neutral', 'feature_vector': []},
    {'corpus': "produto razoável", 'review_type': 'neutral', 'feature_vector': []}         
]
unclassified_review = {
    'corpus': 'parece ser razoável nunca mais compro novamente',
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

X = [] # feature vectors
y = [] # feature classes
for review in classified_reviews:
    X.append(review['feature_vector'])
    y.append(review['review_type'])

classifier = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 3), random_state=1)



classifier.fit(X, y)

print(classifier.predict([unclassified_review['feature_vector']]))
print(classifier.predict_proba([unclassified_review['feature_vector']]))
print(classifier.classes_)

