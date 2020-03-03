# Text retrieve service

from flask import Flask, request
from flask_restful import Resource, Api
from urllib.request import Request, urlopen
import html2text

app = Flask(__name__)
api = Api(app)

class Text(Resource):
    def get(self):
        # get url_path from args
        args = request.args

        req = Request(args['url_path'])

        resource = urlopen(req)
        content = resource.read()
        charset = resource.headers.get_content_charset()
        content = content.decode(charset)

        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_emphasis = True
        h.ignore_images = True
        h.single_line_break = True
        h.skip_internal_links = True
        text = h.handle(content)
        if text:
            return {
                'status': 'success',
                'retrieved_text': text
            }, 200
        else:
            return {'status': 'failure', 'data': None}, 404



# routine
api.add_resource(Text, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
