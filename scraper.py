import requests
import lxml.html as htmll

SITE_URL = 'https://www.larepublica.co/'

XPATH_TREND_NEWS = '//div[@class="containerMostViewed"]/div/ul/li/div[@class="d-flex"]/div[@class="V_Trends"]/a/@href'
XPATH_TOP_SECOND_NEWS = '//div[@class="row row-cols-3"]/div[@class="col mb-4"]/div[@class="news V_Title_Img"]/h2/a/@href'
XPATH_SECOND_NEWS = '//div[@class="row row-cols-3"]/div[@class="col mb-3"]/div/a/@href'

XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


def run():
    pass


if __name__ == '__main__':
    run()
