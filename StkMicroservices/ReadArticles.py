import spacy
from spacy.matcher import Matcher
from bs4 import BeautifulSoup
import requests
from importlib import reload
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

url = 'https://finance.yahoo.com/news/applied-materials-amat-outpaces-stock-214509414.html'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

print(soup.text)
print("********************************************************************************")

nlp = spacy.load("en_core_web_sm")
customer_feedback = open("Receipt.pdf").read()

doc = nlp(customer_feedback)

dep_labels = []
for token in doc:
    while token.head != token:
        dep_labels.append(token.dep_)
        token = token.head
print(dep_labels)

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]
matcher.add('IPHONE_PATTERN', None, pattern)

# Process some text
doc = nlp("New iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)
