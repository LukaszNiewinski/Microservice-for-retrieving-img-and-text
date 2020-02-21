from flask_restful import Resource

class Webpage_text(Resource):
    def get(self, identifier):
        return [
                  {
                    "identifier": identifier,
                    "url_path": "www.google.com",
                    "text": "long text"
                  }
                ], 200


