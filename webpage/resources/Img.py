from flask_restful import Resource

class Img(Resource):
    def get(self, identifier):
        return [
                  {
                    "identifier": identifier,
                    "url_path": "www.google.com",
                    "img": "download img"
                  }
                ], 200


