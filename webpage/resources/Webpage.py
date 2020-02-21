from flask_restful import Resource
from flask import request
import json
import requests
import Model

webpages_schema = Model.WebpageRetrievedSchema(many=True)
webpage_schema = Model.WebpageRetrievedSchema(dump_only=['identifier', 'created_at'])


class Webpage(Resource):
    def get(self):
        # GET method for accessing the data about stored already retrieved websites
        if Model.WebpageRetrieved.query.all():
            webpages = Model.WebpageRetrieved.query.all()
            webpages = webpages_schema.dump(webpages)

            return {'status': 'success, list of all the webpages', 'data': webpages}, 200
        else:
            return {'status': 'failure', 'data': 'None'}, 404

    def post(self):
        # POST method for retrieving text/img from new website (or repeat at other time)
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
            data['url_path'] = response_dict['url_path'][0]
            data['retrieved_text'] = False
            data['retrieved_img'] = False

            if 'text' in to_retrieve:
                data['retrieved_text'] = True
            if 'img' in to_retrieve:
                data['retrieved_img'] = True

        webpage = Model.WebpageRetrieved(data["url_path"], data["retrieved_text"], data["retrieved_img"])


        Model.db.session.add(webpage)
        Model.db.session.commit()

        # add webpage data to the table
        obj = Model.db.session.query(Model.WebpageRetrieved).order_by(Model.WebpageRetrieved.identifier.desc()).first()
        result = webpage_schema.dump(obj)

        #send requests to the containers
        retrieved_text = None
        if data['retrieved_text']:
            try:
                print(data['url_path'])
                r = requests.get('http://text_retrieve?url_path='+data['url_path'])
                retrieved_text = r.json()

            except:
                return {'status': 'failure', 'information': 'text_retrieve failure'}, 404


        if retrieved_text:
            # add retrieved text to the table
            data_text = Model.TextRetrieved(identifier=result['identifier'], text=retrieved_text['retrieved_text'])
            Model.db.session.add(data_text)
            Model.db.session.commit()


        return {'status': 'success', 'webpage': result, 'retrieved_text': retrieved_text}, 201
