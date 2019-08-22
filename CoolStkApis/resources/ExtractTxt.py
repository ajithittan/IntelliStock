from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from bs4 import BeautifulSoup
import requests
import urllib3.request
from resources import utils

class ExtractTxt(Resource):

    url_args = {"inpurl": fields.Str()}

    @use_args(url_args)
    def get(self,inpURL):
        print("am i here????????")
        inpurl = format(inpURL["inpurl"])
        print("what is the url", inpurl)
        response =  requests.get(inpurl)
        html = response.text
        cleaned = utils.cleanme(html)
        print (cleaned)
        return {'CleanContent': cleaned},200

    def post(self):
        return {"message": "Hello, World!"}
