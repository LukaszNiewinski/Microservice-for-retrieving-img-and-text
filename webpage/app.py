
from flask_restful import Resource, Api
from flask import Blueprint
from resources.Webpage import Webpage
from resources.Webpage_text import Webpage_text
from resources.Webpage_img import Webpage_img

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Webpage, '/webpages')
api.add_resource(Webpage_text, '/webpage_text/<string:identifier>')
api.add_resource(Webpage_img, '/webpage_img/<string:identifier>')
