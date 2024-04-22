''' 
Extractive summarization example.
Author: Fabrício Galende M. de Carvalho, DSc

'''
from preprocessing_pipeline import TextNormalizer
from language_model_pipeline import BagOfWords, TfIdfTransform
import spacy

model_spacy =  spacy.load('pt_core_news_sm')
my_documents = [" Adoramos o produto e compraremos de novo.",
                " O produto é ótimo, adorei!!",
                " Gostamos muito do produto!",
                "Vamos comprar o produto novamente!",
                "Comprarei o produto novamente!!",
                "Amamos o produto e achamos que vamos comprar novamente!",
                "O produto é de ótima qualidade. ",
                "Achamos que é um ótimo negócio e ótima qualidade."]

stop_words = ['o', 'a', 'e', 'esse', 'aquele', 'este', 'de', 'do', 'da']
my_text_normalizer = TextNormalizer(stop_words)
my_bow = BagOfWords(my_documents, my_text_normalizer)
my_bow.build_model_lexicon() ## Model lexicon creation
#print("Model lexicon: -------------------------VVVVVV")
#print(my_bow.lexicon)

analized_docs = []
adj_rank = {}
for document in my_documents:
    analysis = {}
    print("Novo documento sendo analisado:.......")
    analysis['original_doc'] = document
    analysis['sentence_lower'] = my_text_normalizer.case_conversion(document)
    analysis['sentence_token'] = my_text_normalizer.sentence_tokenizer(analysis['sentence_lower'])
    analysis['words'] = my_text_normalizer.word_tokenizer(analysis['sentence_token'][0])
    analysis['words_without_stop_words'] =  my_text_normalizer.stop_words_removal(analysis['words'])
    analysis['sentence_pos_tags'] = [ {'word':str(word), 'pos':word.pos_} for word in model_spacy(analysis['sentence_token'][0])]
    #print(analysis['sentence_pos_tags'])
    # Now a document score is built based on model statistics (occurrence in sentences)
    doc_score = 0
    for tag_pair in analysis['sentence_pos_tags']:
        #print("Tag pair: ", tag_pair)
        #if (tag_pair['word'] in my_bow.lexicon):
        #    print("word found in model lexicon")
        if tag_pair['pos'] == 'ADJ' and (tag_pair['word'] in my_bow.lexicon):
            doc_score += my_bow.lexicon[tag_pair['word']]['counter']    
    analysis['doc_score'] = doc_score

    analized_docs.append(analysis)
print("\n\n\n\n -----------------------")

print(analized_docs[1])
print("\n\n\n\-----------")


for doc in analized_docs:   
    print("Document score: ", doc['doc_score'])

print("Documents extractive summary: ")
print(analized_docs[7]['original_doc'])
print(analized_docs[6]['original_doc'])
print(analized_docs[1]['original_doc'])

    





