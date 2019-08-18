from flask_restful import Resource
from bs4 import BeautifulSoup
import requests

class ExtractTxt(Resource):

    def get(self,inpurl):
        print(inpurl)
        req = requests.get(inpurl)
        soup = BeautifulSoup(req.text, 'html.parser')
        return (soup.text)

    def post(self):
        return {"message": "Hello, World!"}
