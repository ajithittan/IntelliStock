import requests
import spacy
from spacy.matcher import Matcher

def extracttextfromhtml(inpUrl):
    resp = requests.get('http://localhost:5000/api/ExtractTxt?inpurl=' + inpUrl)
    return resp.json()

def matchText (inpContent,inpMatcher):

    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)

    #pattern = [inpMatcher]
    #pattern = [{"IS_PUNCT": True},{'lower': inpMatcher}]
    pattern = [{'lower': inpMatcher}]
    matcher.add('INPUT_PATTERN', None, pattern)

    print("Pattern 123",pattern)
    #print(inpContent)

    doc = nlp(inpContent)
    matches = matcher(doc)

    matched_sentences=[]
    for match_id, start, end in matches:
        matched_span = doc[start:end]
        matched_sentences.append(matched_span.text)
        print("matched text",matched_span.text)

    return matched_sentences
