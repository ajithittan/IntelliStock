from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
import bs4 as bs
import requests
import urllib.request
#import re
from resources import utils

class ExtractTxt(Resource):

    url_args = {"inpurl": fields.Str()}

    @use_args(url_args)
    def get(self,inpURL):
        print("am i here????????")
        inpurl = format(inpURL["inpurl"])
        #print("what is the url", inpurl)
        #response =  requests.get(inpurl)
        #html = response.text
        #cleaned = utils.cleanme(html)
        #print (cleaned)
        scrapped_data = urllib.request.urlopen(inpurl)
        article = scrapped_data.read()
        parsed_article = bs.BeautifulSoup(article,'lxml')
        paragraphs = parsed_article.find_all('p')
        #print(paragraphs)
        article_text = ""

        for p in paragraphs:
            article_text += p.text

        processed_article = article_text.lower()
        #processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
        #processed_article = re.sub(r'\s+', ' ', processed_article)
        print(processed_article)
        return {'CleanContent': processed_article},200

    def post(self):
        return {"message": "Hello, World!"}
