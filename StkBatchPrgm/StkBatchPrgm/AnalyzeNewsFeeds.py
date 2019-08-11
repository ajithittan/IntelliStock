import spacy
import urllib.request
from bs4 import BeautifulSoup

response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

nlp = spacy.load('en',disable = ['ner'])
nlp.max_length = 93621305
#doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

customer_feedback = open("Receipt.pdf","r",encoding='utf-8', errors='ignore').read()
doc = nlp(customer_feedback)
print(doc.json())
