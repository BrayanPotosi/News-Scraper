import lxml.html as html
from datetime import date
import requests
import os

SITE_URL = 'https://www.larepublica.co/'

XPATH_TREND_NEWS = '//div[@class="containerMostViewed"]/div/ul/li/div[@class="d-flex"]/div[@class="V_Trends"]/a/@href'
XPATH_TOP_SECOND_NEWS = '//div[@class="col mb-4"]/div[@class="news V_Title_Img"]/h2/a/@href'
XPATH_SECOND_NEWS = '//div[@class="row row-cols-3"]/div[@class="col mb-3"]/div/a/@href'

XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'


def get_title(link):
    url = link.split('/')[-1]
    title_list = url.split('-')[:-1]
    title = " ".join(title_list)
    return title


def parse_notice(link, folder_title):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)
            try:
                title = get_title(link)
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)

            except IndexError:
                return

            with open(f'{folder_title}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(f'{title}\n\n\n')
                f.write(f'{summary}\n\n\n')
                for p in body:
                    f.write(f'{p}\n')

        else:
            raise ValueError(f'Error, status code {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(SITE_URL)

        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            list_links = parsed.xpath(XPATH_SECOND_NEWS)
            current_date = date.today().strftime('%d-%m-%Y')
            folder_title = f'la_replublica_news_{current_date}'

            if not os.path.isdir(folder_title):
                os.mkdir(folder_title)

            for link in list_links:
                parse_notice(link, folder_title)

        else:
            raise ValueError(f'Error, status code: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()
