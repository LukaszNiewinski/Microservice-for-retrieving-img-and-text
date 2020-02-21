from flask_restful import Resource
from flask import request
import Model
import json

webpages_schema = Model.WebpageRetrievedSchema(many=True)
webpage_schema = Model.WebpageRetrievedSchema(dump_only=['identifier', 'created_at'])

class Webpage(Resource):
    def get(self):
        if Model.WebpageRetrieved.query.all():
            webpages = Model.WebpageRetrieved.query.all()
            webpages = webpages_schema.dump(webpages)

            return {'status': 'success, list of all the webpages', 'data': webpages}, 200
        else:
            return {'status': 'failure', 'data': 'None'}, 404

    def post(self):
        #get data from web form request
        try:
            # get data from api request
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400

            parsed_json = json.loads(json.dumps(json_data[0]))
            # Validate and deserialize input
            data = webpage_schema.load(parsed_json)
        except:
            # get data posted through website form
            response_dict = request.form.to_dict(flat=False)
            to_retrieve = response_dict['retrieve']

            data = {}
            data['url_path'] = response_dict['url_path']
            data['retrieved_text'] = False
            data['retrieved_img'] = False

            if 'text' in to_retrieve:
                data['retrieved_text'] = True
            if 'img' in to_retrieve:
                data['retrieved_img'] = True

        webpage = Model.WebpageRetrieved(data["url_path"], data["retrieved_text"], data["retrieved_img"])

        Model.db.session.add(webpage)
        Model.db.session.commit()

        obj = Model.db.session.query(Model.WebpageRetrieved).order_by(Model.WebpageRetrieved.identifier.desc()).first()
        result = webpage_schema.dump(obj)

        return {'status': 'successfully created, data will be retrieved', 'data': result}, 201
