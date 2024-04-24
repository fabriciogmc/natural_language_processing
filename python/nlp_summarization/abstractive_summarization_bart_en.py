from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Input text to be summarized (from wikipedia)
input_text = """
Natural language processing (NLP) is an interdisciplinary subfield of 
computer science and information retrieval. It is primarily concerned 
with giving computers the ability to support and manipulate human language.
It involves processing natural language datasets, such as text corpora or
speech corpora, using either rule-based or probabilistic (i.e. statistical and,
 most recently, neural network-based) machine learning approaches. 
 The goal is a computer capable of "understanding" the contents
 of documents, including the contextual nuances of the language within them. 
 To this end, natural language processing often borrows ideas from theoretical 
 linguistics. The technology can then accurately extract information and insights
 contained in the documents as well as categorize and organize the documents
 themselves.
"""

# Tokenize and summarize the input text using BART
inputs = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs, max_length=80, min_length=10, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decode and output the summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Original Text:")
print(input_text)
print("\nSummary:")
print(summary)