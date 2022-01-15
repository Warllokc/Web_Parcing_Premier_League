import requests
import json
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import webbrowser, os
# from PIL import Image

URL = 'https://www.premierleague.com/players'

page = requests.get(URL, auth=HTTPBasicAuth('warllokc@yahoo.com', 'Petrici-89'))
soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find_all("tbody", class_="dataContainer indexSection")

# test from book
players_table =soup.select('.playerName')
# print((type(players_table)))
# print(len(players_table))
# print(type(players_table[0]))
# print(str(players_table[0]))
# res = players_table[0].getText()
# print(res)
dictionary_with_elements_attr = players_table[0].attrs
# print(dictionary_with_elements_attr.get('href'))
empty_player_dictionary = {}
for players in players_table:
    empty_player_dictionary[players_table[0].getText()] = dictionary_with_elements_attr.get('href')

print(empty_player_dictionary)





# res = json.dumps(page.text)
#
# print(len(res))

# requests.put()

code = page.status_code

print(code)
