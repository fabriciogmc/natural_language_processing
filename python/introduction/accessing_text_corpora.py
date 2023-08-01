# Accessing text corpora example.

from nltk.corpus import wordnet

word = 'help'

# Getting synonyms:
word_synsets = wordnet.synsets(word)


for synset in word_synsets:
    print(("Synset Name: {name}\n"
           "POS Tag: {tag} \n"
           "Definition: {definition}\n"
           "Examples: {examples}\n").format(name=synset.name(),
                                           tag=synset.pos(),
                                           definition = synset.definition(),
                                           examples = synset.examples()))
    

print("Language supported:", wordnet.langs())
print(wordnet.synset('dog.n.01').lemma_names('ita'))

print(wordnet.lemma_count("Processor"))

#print(word_synonyms)