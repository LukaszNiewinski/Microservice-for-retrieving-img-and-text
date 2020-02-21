from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object("project.config.Config")

db = SQLAlchemy(app)
ma = Marshmallow(app)
