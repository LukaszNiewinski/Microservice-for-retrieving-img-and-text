from flask_restful import Resource
from flask import request
import json
import requests
import Model

text_retrieved_schema = Model.TextRetrievedSchema(dump_only=['id'])

class Text(Resource):
    def get(self):
        try:
            # get identifier from args
            args = request.args
            identifier = args['identifier']

            text_retrieved = Model.TextRetrieved.query.filter_by(identifier=identifier).first()
            data = text_retrieved_schema.dump(text_retrieved)
            if data:
                return {'status': 'success', 'data': data}, 200
            else:
                return {'status': 'failure', 'data': 'None'}, 404
        except:
            return {'status': 'failure', 'information': 'perhaps entry does not exist'}, 404




