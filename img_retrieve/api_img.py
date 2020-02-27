# Text retrieve service
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from flask import Flask, request
from flask_restful import Resource, Api

from multiprocessing import Process, Manager
import json

app = Flask(__name__)
api = Api(app)


def run_retrieve(url, result):
    def crawler_results(signal, sender, item, response, spider):
        result.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())

    process.crawl('img_retrieve', start_url=url)
    # process.crawl('img_retrieve', start_url="https://www.wp.pl")
    process.start()  # the script will block here until the crawling is finished
    process.join()



class Img(Resource):
    def get(self):
        # get url_path and retrieve identifier from args
        args = request.args
        url_path = args['url_path']
        identifier = args['identifier']

        manager = Manager()
        result = manager.list()

        paths = []

        new_process = Process(target=run_retrieve, args=(url_path, result))
        new_process.start()
        new_process.join()

        if result:
            print("KUUUUUUUPA")
            print(result[0]['images'])
            for img in result[0]['images']:
                paths.append('https://microservice-images.s3.eu-central-1.amazonaws.com/' + img['path'])
        else:
            paths = [None]

        return {'data': url_path, 'identifier': identifier, 'img_paths': paths}, 200

# routine
api.add_resource(Img, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
