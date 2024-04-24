"""
Exemplifying extractive summarization with summy library
"""
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Example text
texto = """
O produto em questão é de ótima qualidade.
A qualidade pode ser avaliada pela durabilidade, adequado encaixe das peças
e facilidade de montagem. Dessa forma, pode-se afirmar que o resultado foi
totalmente satisfatório. Definitivamente voltarei a comprar o produto pois, agora,
sou um cliente satisfeito.
"""

# Building text parser
parser = PlaintextParser.from_string(texto, Tokenizer("portuguese"))

# Building a LSA summarizer (Latent Semantic Analysis)
summarizer = LsaSummarizer()

# Building the summary with 2 sentences
summary= summarizer(parser.document, 2)

# Summary:
for sentence in summary:
    print(sentence)