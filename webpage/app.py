
from flask_restful import Resource, Api
from flask import Blueprint
from resources.Webpage import Webpage

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Webpage, '/Webpage')
