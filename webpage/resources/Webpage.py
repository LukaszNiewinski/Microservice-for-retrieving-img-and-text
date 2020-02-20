from flask_restful import Resource

class Webpage(Resource):
    def get(self):
        return {"webpage": "url get"}

    def post(self):
        return {"webpage": "url post"}

