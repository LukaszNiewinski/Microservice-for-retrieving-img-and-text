
from flask import render_template, request, url_for, Blueprint
import requests
from project import app
import Model

views = Blueprint('views', __name__)

# initial application page
@app.route('/')
def home():
    return render_template('home.html')

# Order retrieving new webpage through the web browser
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


# GET information about retrieved pages and check it's identifiers
@app.route('/get_data')
def get_data():
    webpages_schema = Model.WebpageRetrievedSchema(many=True)

    if Model.WebpageRetrieved.query.all():
        webpages = Model.WebpageRetrieved.query.all()
        webpages = webpages_schema.dump(webpages)

        return render_template('get_data.html', result=webpages)
    else:
        # for improvement - crashes when not any entries in db
        return render_template('get_data.html')
