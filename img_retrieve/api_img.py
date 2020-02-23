# Text retrieve service

from flask import Flask, request
from flask_restful import Resource, Api
from scrapy.crawler import CrawlerRunner
from scrapy_img.scrapy_img.spiders.ImgSpider import ImgSpider
from twisted.internet import reactor


app = Flask(__name__)
api = Api(app)

class Img(Resource):
    def get(self):
        # get url_path and retrieve identifier from args
        args = request.args
        url_path = args['url_path']
        identifier = args['identifier']
        # initiate retrieving images from given url
        # img_spider = ImgSpider(start_url=url_path)


        # [TO DO] makre crawler great again(fix it)
        # runner = CrawlerRunner()
        # d = runner.crawl(ImgSpider, start_url=url_path)
        # d.addBoth(lambda _: reactor.stop())
        # reactor.run()


        # [TO DO] return images paths
        img_paths = None
        return {'data': url_path, 'identifier': identifier, 'img_paths': None}

# routine
api.add_resource(Img, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
