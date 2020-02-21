
from flask_restful import Resource, Api
from flask import Blueprint
from resources.Webpage import Webpage
from resources.Text import Text
from resources.Img import Img


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Webpage, '/webpages')
api.add_resource(Text, '/text')
api.add_resource(Img, '/img')
