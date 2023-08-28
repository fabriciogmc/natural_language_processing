'''
BeautifulSoup api example

Author: Fabrício Galende M. de Carvalho, DSc
'''
from bs4 import BeautifulSoup

noisy_text = '''
<body>
<p>Sentence 1. </p>
<p>Sentence 2. </p>
<p>Sentence 3. </p>
<script> var x = 1; </script>
<iframe> contents... </iframe>
<p>Sentence 4. </p>
<body>
'''
soup = BeautifulSoup(noisy_text, "html.parser")
[s.extract() for s in soup(['iframe'])]

print("Noisy text: ")
print(noisy_text)
print("Clean text:")
print(soup.get_text())