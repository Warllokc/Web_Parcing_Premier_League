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


empty_player_dictionary = {}

def scrape_player_data():
    id = 1
    while True:

        empty_player_dictionary["id"] = id

        URL = "https://www.premierleague.com/players/" + str(id)

        headers = {"accept": "*/*",
               "accept-language": "en-US,en;q=0.9",
               "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
               "origin": "https://www.premierleague.com",
               "referer": "https://www.premierleague.com/",
               "sec-ch-ua": 'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
               "sec-ch-ua-mobile": "?0",
               "sec-ch-ua-platform": "Windows",
               "sec-fetch-dest": "empty",
               "sec-fetch-mode": "cors",
               "sec-fetch-site": "cross-site",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36}"}

        rec = requests.get(url=URL, headers=headers)
        if rec.status_code == 200:
            soup = BeautifulSoup(rec.content, "html.parser")
            player_data = soup.findAll("div", class_ ="info")
            player_country = soup.findAll("span", class_ ="playerCountry")

            ########
            # if not player_data[0].next:
            #     id+=1
            # #######

            picture = soup.findAll('img')[42]

            # Adding to dictionary name, country of origin
            empty_player_dictionary["name"] = picture.get('alt')
            empty_player_dictionary["country"] = player_country[0].next

            if "Photo-Missing" in picture.get('src') and picture.get('data-player'):
                a_string = str(picture.get('src')).replace("Photo-Missing", str(picture.get('data-player')))

            # Adding to dictionary image_link
                empty_player_dictionary["image_link"] = a_string.replace("//", "")
            else:

            # Adding to dictionary image_link
                empty_player_dictionary["image_link"] = picture.get('src').replace("//", "")

            # Adding to dictionary position, date of birth, height and link
            empty_player_dictionary["position"] = player_data[0].next
            empty_player_dictionary["date_of_birth"] = player_data[2].next.strip()
            empty_player_dictionary["height"] = player_data[3].next
            empty_player_dictionary["player_link"] = URL

            id += 1


            print(empty_player_dictionary)

        else:
            print("end of Parsing")
            break
        if id == 30 or id == 120:
            id += 2
        elif id == 63 or id ==90 or id == 144:
            id+=1

scrape_player_data()

