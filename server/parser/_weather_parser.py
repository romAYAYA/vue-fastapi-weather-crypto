import requests
from bs4 import BeautifulSoup


def get_temp(city: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5',
        'Referer': 'https://yandex.kz/',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    res = requests.get(f'https://pogoda.co.il/kazakhstan/{city}', headers=headers)
    weather_soup = BeautifulSoup(res.text, 'html.parser')

    temp = weather_soup.find('strong').get_text(strip=True)

    if temp:
        return temp
    else:
        return 'An error occurred, temprature or city was not found'

