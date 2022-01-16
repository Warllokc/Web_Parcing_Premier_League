import requests
import json
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

URL = 'https://www.premierleague.com/players'

page = requests.get(URL, auth=HTTPBasicAuth('login', 'password'))
soup = BeautifulSoup(page.content, "html.parser")
players_table =soup.select('.playerName')
print((type(players_table)))
print(len(players_table))


empty_player_dictionary = {}
def scrape_Player_data():
    index_player = 0
    for players in players_table:
        dictionary_with_elements_attr = players_table[index_player].attrs
        empty_player_dictionary[players_table[index_player].getText()] = dictionary_with_elements_attr.get('href')
        index_player+=1

scrape_Player_data()
print(empty_player_dictionary)
print(len(empty_player_dictionary))


# res = json.dumps(page.text)
# print(len(res))
# requests.put()
code = page.status_code

print(code)
