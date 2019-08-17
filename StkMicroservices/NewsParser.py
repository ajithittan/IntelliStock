import spacy
from spacy.matcher import Matcher

class textMatcher:

    def matchText (self,inpContent,inpMatcher):

        nlp = spacy.load('en_core_web_sm')
        matcher = Matcher(nlp.vocab)

        pattern = [inpMatcher]
        matcher.add('INPUT_PATTERN', None, pattern)

        doc = nlp(inpContent)
        matches = matcher(doc)

        matched_sentences[]
        for match_id, start, end in matches:
            matched_span = doc[start:end]
            matched_sentences.append(atched_span.text)
            print(matched_span.text)

        return matched_sentences
