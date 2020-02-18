# Text retrieve service

from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

# class Nowy(Resource):
#     def get(self):
#         # to return text data.. in JSON??
#         return {
#             'nowy': ['some ccct', 'volume test2',]
#         }
#
# # routine
# api.add_resource(Nowy, '/')

@app.route('/')
def get():
    img_j = requests.get('http://img_retrieve').json()

    text_j = requests.get('http://text_retrieve').json()

    return text_j


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
