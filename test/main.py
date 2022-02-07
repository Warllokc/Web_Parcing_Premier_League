
import json

import grequests

from bs4 import BeautifulSoup

import sql_alchemy_table as sql_table

empty_player_list = []

STEP = 50

URL = "https://www.premierleague.com/players/"
HEDERS = {"accept": "*/*",
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

# ADDING PLAYERS DATA TO JSON FILE


def get_async_data(urls):
    reqs = [grequests.get(link, headers=HEDERS) for link in urls]
    responses = grequests.map(reqs)
    return responses


def pareser_add_json(data):

    try:
        soup = BeautifulSoup(data.content, "html.parser")
        player_data = soup.findAll("div", class_="info")
        player_country = soup.findAll("span", class_="playerCountry")
        picture = soup.findAll('img')[42]
        # Adding to the list image_link
        if "Photo-Missing" in picture.get('src') and picture.get('data-player'):
            a_string = str(picture.get('src')).replace("Photo-Missing", str(picture.get('data-player')))
            photo = a_string.replace("//", "")
        else:
            photo = picture.get('src').replace("//", "")
        # Adding to the list name, country, image_link, position, date of birth, height and player_link
        empty_player_list.append({"name": picture.get('alt'),
                                 "country": player_country[0].next,
                                 "image_link": photo,
                                 "position": player_data[0].next,
                                  "date_of_birth": player_data[2].next.strip(),
                                  "height": player_data[3].next,
                                  "player_link": data.url
        })
        print(f"{empty_player_list}")

    except:
        pass


def add_to_json(data):
    with open("players.json", "a") as outfile:
        outfile.write(json.dumps(data, indent=4))


def scrape_player_data_json():
    list_a = [f"{URL}{count}" for count in range(1, 2000)]
    output = [list_a[i:i + STEP] for i in range(0, len(list_a), STEP)]
    for url in output:
        for resopnd in get_async_data(url):
            if resopnd and resopnd.status_code == 200:
                pareser_add_json(resopnd)


# SCRAPE AND ADD DATA TO JSON FILE
# scrape_player_data_json()
# add_to_json(empty_player_list)


# ADDING PLAYERS DATA TO DB

def pareser_add_to_db(data):
    try:
        soup = BeautifulSoup(data.content, "html.parser")
        player_data = soup.findAll("div", class_="info")
        player_country = soup.findAll("span", class_="playerCountry")
        picture = soup.findAll('img')[42]
        # Adding to the list image_link
        if "Photo-Missing" in picture.get('src') and picture.get('data-player'):
            a_string = str(picture.get('src')).replace("Photo-Missing", str(picture.get('data-player')))
            photo = a_string.replace("//", "")
        else:
            photo = picture.get('src').replace("//", "")
        # Adding to to db, country, image_link, position, date of birth, height and player_link
        sql_table.add_player_data(picture.get('alt'), player_country[0].next, photo, player_data[0].next,
                                  player_data[2].next.strip(), player_data[3].next, data.url)

        print(f"{picture.get('alt')} added to DB")

    except:
        pass


def scrape_player_data_to_db():
    list_a = [f"{URL}{count}" for count in range(1, 2000)]
    output = [list_a[i:i + STEP] for i in range(0, len(list_a), STEP)]
    for url in output:
        for resopnd in get_async_data(url):
            if resopnd and resopnd.status_code == 200:
                pareser_add_to_db(resopnd)


# SCRAPE AND ADD DATA TO DB
scrape_player_data_to_db()