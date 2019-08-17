from flask_restful import Resource

class ExtractTxt(Resource):

    def get(self):
        return {"message": "Yes, World!"}

    def post(self):
        return {"message": "Hello, World!"}
