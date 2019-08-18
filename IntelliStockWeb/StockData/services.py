import requests

def extracttextfromhtml(inpUrl):
    resp = requests.get('http://localhost:5000/api/ExtractTxt')
    return resp
