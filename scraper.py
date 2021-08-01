import requests
import lxml.html as html

SITE_URL = 'https://www.larepublica.co/'

XPATH_TREND_NEWS = '//div[@class="containerMostViewed"]/div/ul/li/div[@class="d-flex"]/div[@class="V_Trends"]/a/@href'
XPATH_TOP_SECOND_NEWS = '//div[@class="col mb-4"]/div[@class="news V_Title_Img"]/h2/a/@href'
XPATH_SECOND_NEWS = '//div[@class="row row-cols-3"]/div[@class="col mb-3"]/div/a/@href'

XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


def parse_home():
    try:
        response = requests.get(SITE_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            link_news = parsed.xpath(XPATH_TOP_SECOND_NEWS)
            for new in link_news:
                print(new)
        else:
            raise ValueError(f'Error, status code: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()
