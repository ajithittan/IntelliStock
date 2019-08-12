import spacy
import urllib.request
from bs4 import BeautifulSoup

response =  urllib.request.urlopen('https://finance.yahoo.com/news/making-sense-market-191107758.html')
html = response.read()
#print(html)

soup = BeautifulSoup(html,"lxml")
text = soup.get_text()
#print(soup.prettify())
print(text)

nlp = spacy.load('en',disable = ['ner'])
nlp.max_length = 93621305
#doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

customer_feedback = open("Receipt.pdf","r",encoding='utf-8', errors='ignore').read()
doc = nlp(customer_feedback)
#print(doc.json())
