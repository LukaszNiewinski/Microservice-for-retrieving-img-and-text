import datetime
from marshmallow import Schema, fields, pre_load, validate, post_load
from sqlalchemy.orm import backref

import project

db = project.db
ma = project.ma


class WebpageRetrieved(db.Model):
    __tablename__ = 'webpages_retrieved'
    identifier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_path = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)
    retrieved_text = db.Column(db.Boolean, default=True)
    retrieved_img = db.Column(db.Boolean, default=True)
    # set one-to-one relationship with text_retrieved
    textretrieved = db.relationship("TextRetrieved", backref=backref('webpages_retrieved', uselist=False))
    # set one-to-many relationships with img_retrieved (possibility of many img per site)
    img_retrieved = db.relationship("ImgRetrieved", backref="webpages_retrieved")

    def __init__(self, url_path, retrieved_text, retrieved_img):
        self.url_path = url_path
        self.retrieved_text = retrieved_text
        self.retrieved_img = retrieved_img

class TextRetrieved(db.Model):
    __tablename__ = 'text_retrieved'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.Integer, db.ForeignKey('webpages_retrieved.identifier', ondelete='CASCADE'), nullable=False)
    text = db.Column(db.UnicodeText)

    def __init__(self, identifier, text):
        self.identifier = identifier
        self.text = text

class ImgRetrieved(db.Model):
    __tablename__ = 'img_retrieved'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.Integer, db.ForeignKey('webpages_retrieved.identifier', ondelete='CASCADE'), nullable=False)
    img_path = db.Column(db.String(250), nullable=False)

    def __init__(self, identifier, img_path):
        self.identifier = identifier
        self.img_path = img_path


# marshmallow schema for validation and serialization/deserialization
class WebpageRetrievedSchema(ma.Schema):
    class Meta:
        model = WebpageRetrieved


    identifier = fields.Integer()
    url_path = fields.Url()
    created_at = fields.DateTime(default=datetime.datetime.utcnow())
    retrieved_text = fields.Boolean()
    retrieved_img = fields.Boolean()




class TextRetrievedSchema(ma.Schema):
    id = fields.Integer(required=True)
    identifier = fields.Integer(required=True)
    text = fields.String(required=True)


class ImgRetrievedSchema(ma.Schema):
    id = fields.Integer(required=True)
    identifier = fields.Integer(required=True)
    img_path = fields.String(required=True)

db.init_app(project.app)
