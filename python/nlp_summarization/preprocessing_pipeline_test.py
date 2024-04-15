from preprocessing_pipeline import TextNormalizer

my_doc = "Esse produto é      muito, bom! Adorei!"
my_normalizer = TextNormalizer()

# Sentence tokenization 
sentences = my_normalizer.sentence_tokenizer(my_doc)
print(sentences)

# word tokenization
words = my_normalizer.word_tokenizer(sentences[0])
print(words)
