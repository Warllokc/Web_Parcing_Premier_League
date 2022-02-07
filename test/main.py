
import json

import grequests

from bs4 import BeautifulSoup



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


def get_async_data(urls):
    reqs = [grequests.get(link, headers=HEDERS) for link in urls]
    responses = grequests.map(reqs)
    return responses


def pareser(data):
    empty_player_dictionary = {}
    test = []
    try:
        soup = BeautifulSoup(data.content, "html.parser")
        player_data = soup.findAll("div", class_="info")
        player_country = soup.findAll("span", class_="playerCountry")
        picture = soup.findAll('img')[42]

        # Adding to dictionary name, country of origin
        empty_player_dictionary["name"] = picture.get('alt')
        empty_player_dictionary["country"] = player_country[0].next
        test.append({"name": picture.get('alt'), "country": player_country[0].next})


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
        empty_player_dictionary["player_link"] = data.url

        print(f"{empty_player_dictionary}")

        add_to_json(empty_player_dictionary)

    except:
        pass


def add_to_json(data):
    with open("players.json", "a") as outfile:
        outfile.write(json.dumps(data, indent=4, separators=(",","=")))


def scrape_player_data():
    list_a = [f"{URL}{count}" for count in range(1, 2000)]
    output = [list_a[i:i + STEP] for i in range(0, len(list_a), STEP)]
    for url in output:
        for resopnd in get_async_data(url):
            if resopnd and resopnd.status_code == 200:
                pareser(resopnd)



scrape_player_data()
