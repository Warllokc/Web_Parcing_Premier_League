import requests
import json

URL = 'https://api.publicapis.org/entries'

r = requests.get(URL)
# print(r.text)
res = json.dumps(r.text)

print(len(res))

# requests.put()

code = r.status_code

print(code)
# print(r.status_code)
