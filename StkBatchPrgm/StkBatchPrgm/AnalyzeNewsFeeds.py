import spacy

nlp = spacy.load('en',disable = ['ner'])
nlp.max_length = 93621305
#doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

customer_feedback = open("Receipt.pdf","r",encoding='utf-8', errors='ignore').read()
doc = nlp(customer_feedback)
print(doc.json())


#doc.to_disk("/tmp/customer_feedback_627.bin")
#new_doc = Doc(Vocab()).from_disk("/tmp/customer_feedback_627.bin")

#print(new_doc.json())

#for token in doc:
#    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#          token.shape_, token.is_alpha, token.is_stop)
