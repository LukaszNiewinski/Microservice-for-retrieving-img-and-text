from flask_restful import Resource

class Webpage_img(Resource):
    def get(self, identifier):
        return [
                  {
                    "identifier": identifier,
                    "url_path": "www.google.com",
                    "img": "download img"
                  }
                ], 200


