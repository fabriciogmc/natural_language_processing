''' 
HTML tag removal gets rid of textual noise
that do no add meaninful information to document's
content.

Author: Fabrício G. M. de Carvalho, DSc
Adapted from: "Text Analytics with python, Sarkar"
'''

import requests
import re
from bs4 import BeautifulSoup

# a function to get rid of html tags
def get_rid_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    # iframe and script nodes removal from doc tree
    [s.extract() for s in soup(['iframe','script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]','\n',stripped_text)
    return stripped_text

data = requests.get("http://gutenberg.org/cache/epub/8001/pg8001.html")
#data = requests.get("https://gutenberg.org/cache/epub/55682/pg55682-images.html")
content = data.content
soup = BeautifulSoup(content, "html.parser")
clean_content = get_rid_html_tags(soup.get_text())
print(clean_content[1:1000])
