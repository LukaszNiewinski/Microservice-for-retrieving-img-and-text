import scrapy
from ..items import ScrapyImgItem

class ImgSpider(scrapy.spiders.Spider):
    name = "img_spider"

    # initiate spider with start_url
    def __init__(self, *args, **kwargs):
      super(ImgSpider, self).__init__(*args, **kwargs)

      self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        image = ScrapyImgItem()
        img_urls = []

        for img in response.css(".entry-featured-image-url img::attr(src)").extract():
            img_urls.append(img)

        image["image_urls"] = img_urls

        return image
