import scrapy
from ..items import ImgRetrieveItem

class ImgRetrieveSpider(scrapy.spiders.Spider):
    name = "img_retrieve"

    def __init__(self, start_url):
        self.start_urls = [start_url]

    def parse(self, response):
        image = ImgRetrieveItem()
        img_urls = []

        for img in response.css("img::attr(src)").extract():
            # handles wikipedia upload and static files paths
            if img.startswith("//upload"):
                img_urls.append("https:"+img)
            elif 'static' in img:
                url = self.start_urls[0].split("//")[-1].split("/")[0]
                img_urls.append("https://"+url+img)
            elif img.startswith("https://"):
                img_urls.append(img)

        image["image_urls"] = img_urls

        yield image
