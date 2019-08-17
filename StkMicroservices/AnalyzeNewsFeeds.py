import spacy
import urllib.request
from bs4 import BeautifulSoup
import lxml.html.clean


def cleanme(content):
    cleaner = lxml.html.clean.Cleaner(
        allow_tags=[''],
        remove_unknown_tags=False,
        style=True,
    )
    html = lxml.html.document_fromstring(content)
    html_clean = cleaner.clean_html(html)
    return html_clean.text_content().strip()

response =  urllib.request.urlopen('https://finance.yahoo.com/news/apple-chipmakers-soar-following-news-141608172.html')
html = response.read()
#print(html)

cleaned = cleanme(html)
print (cleaned)

nlp = spacy.load("en_core_web_sm")
doc = nlp(cleaned)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

print("*********************************************")

for token in doc:
    print(token.text, token.pos_, token.dep_)

print("----------------------------------------------")
sents_list = []
for sent in doc.sents:
    sents_list.append(sent.text)

for possible_subject in doc:
    print(possible_subject)
#print(sents_list)

soup = BeautifulSoup(html,"lxml")
text = soup.get_text()
#print(soup.prettify())
#print(text)

nlp = spacy.load('en',disable = ['ner'])
nlp.max_length = 93621305
#doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

customer_feedback = open("Receipt.pdf","r",encoding='utf-8', errors='ignore').read()
doc = nlp(customer_feedback)
#print(doc.json())
