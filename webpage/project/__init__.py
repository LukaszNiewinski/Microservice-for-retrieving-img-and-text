from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests

app = Flask(__name__)
app.config.from_object("project.config.Config")


db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/')
def home():
    # img_j = requests.get('http://img_retrieve').json()
    #
    # text_j = requests.get('http://text_retrieve').json()

    return render_template('home.html')


@app.route('/retrieve_data', methods=['GET', 'POST'])
def retrieve_data():
    if request.method == 'POST':

        # to get all the values from checkboxes it needs to be in dict format
        response_dict = request.form.to_dict(flat=False)
        to_retrieve = response_dict['retrieve']
        url_path = response_dict['url_path']
        print(to_retrieve, url_path)
        # [TO DO] connect to containers and order retrieve data
        return response_dict
    else:
        return render_template('retrieve_data.html')


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    # img_j = requests.get('http://img_retrieve').json()
    #
    # text_j = requests.get('http://text_retrieve').json()

    return render_template('get_data.html')
