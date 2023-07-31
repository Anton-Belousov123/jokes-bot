import requests
import bs4


def get_story():
    response = requests.get('https://www.anekdot.ru/random/story/')
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    text = soup.find_all('div', {'class': 'topicbox'})[1].find('div', {'class': 'text'}).text
    if len(text) > 750:
        return get_story()
    return text


