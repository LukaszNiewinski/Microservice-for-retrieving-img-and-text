# Text retrieve service

from flask import Flask, render_template, url_for, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    img_j = requests.get('http://img_retrieve').json()

    text_j = requests.get('http://text_retrieve').json()

    return render_template('home.html')

@app.route('/retrieve_data', methods=['GET','POST'])
def retrieve_data():
    if request.method == 'POST':

        # to get all the values from checkboxes it needs to be in dict format
        response_dict = request.form.to_dict(flat=False)
        to_retrieve = response_dict['retrieve']
        url_path  = response_dict['url_path']
        print(to_retrieve, url_path)


        return response_dict
    else:
        return render_template('retrieve_data.html')


@app.route('/get_data', methods=['GET','POST'])
def get_data():
    img_j = requests.get('http://img_retrieve').json()

    text_j = requests.get('http://text_retrieve').json()

    return render_template('get_data.html')



# add form for taking the data

# define API method to get url addres, text flag(if to retrieve text, and img flag if to retrieve img)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
