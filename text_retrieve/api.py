# Text retrieve service

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Text(Resource):
    def get(self):
        # to return text data.. in JSON??
        return {
            'text': ['some ccct', 'volume test2',]
        }

# routine
api.add_resource(Text, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
