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

import main


#TODO: Scroll through entire page
#
chromedriver_service = Service("C:\\Users\\alexandr\\Downloads\\chromedriver\\chromedriver.exe")
chrome_option = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=chromedriver_service, options=chrome_option)
browser.get(main.URL)
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
                main.scrape_Player_data()
                print(main.empty_player_dictionary)
                print(len(main.empty_player_dictionary))
                break



scrolling()


#TODO: to find elements in the browser
# cookie_page_text = "Accept All Cookies"
# browser.find_element(By.PARTIAL_LINK_TEXT, cookie_page_text).click()
