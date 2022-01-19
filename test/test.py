import requests
import json
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import time

import requests
import json
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import test
URL = 'https://www.premierleague.com/players'

page = requests.get(URL, auth=HTTPBasicAuth('warllokc@yahoo.com', 'Petrici-89'))
soup = BeautifulSoup(page.content, "html.parser")
players_table =soup.select('.playerName')
# print((type(players_table)))
# print(len(players_table))



# TODO: Collect data from entire list of players

empty_player_dictionary = {}
def scrape_Player_data():
    index_player = 0
    for players in players_table:
                dictionary_with_elements_attr = players_table[index_player].attrs
                empty_player_dictionary[players_table[index_player].getText()] = "https://www.premierleague.com" + dictionary_with_elements_attr.get('href')
                index_player+=1

scrape_Player_data()
print(empty_player_dictionary)
print(len(empty_player_dictionary))


# res = json.dumps(page.text)
# print(len(res))
# requests.put()

print(page.status_code)



#TODO: Scroll through entire page
#
chromedriver_service = Service("C:\\Users\\alexandr\\Downloads\\chromedriver\\chromedriver.exe")
chrome_option = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver_service, options=chrome_option)
browser.get(test.URL)
time.sleep(3)
browser.maximize_window()

def scrolling():
    no_of_pagedowns = True
    iframe = browser.find_element(By.CLASS_NAME, 'playerName')
    while no_of_pagedowns:
        try:
            # time.sleep(0.5)
            iframe.send_keys(Keys.PAGE_DOWN)

        except StaleElementReferenceException:
                scrolling()

        except ElementNotInteractableException:
                # scrolling()
                print("Reached bottom of page")
                scrape_Player_data()
                print(empty_player_dictionary)
                print(len(empty_player_dictionary))
                break



scrolling()


#TODO: to find elements in the browser
# cookie_page_text = "Accept All Cookies"
# browser.find_element(By.PARTIAL_LINK_TEXT, cookie_page_text).click()
