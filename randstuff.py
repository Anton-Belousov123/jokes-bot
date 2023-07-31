import requests
import bs4


def get_joke():
    response = requests.get('https://randstuff.ru/joke/').text
    soup = bs4.BeautifulSoup(response, features='html.parser')
    return soup.find('table', {'class': 'text'}).text

