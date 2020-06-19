import requests
import json

url1 = 'https://static.coincap.io/assets/icons/'
url2 = '@2x.png'
URL_data = 'https://api.coincap.io/v2/assets?limit=1000'
fileTail = '.png'

response = requests.get(URL_data)
if response.status_code == 200:
    json = response.json()

for i in range(1000):
    name = json['data'][i]['symbol'].lower()
    new_url = url1 + name + url2
    fileName = name.upper() + fileTail

    res = requests.get(new_url)
    if res.status_code == 200:
        with open(fileName, 'wb') as imgFile:
            imgFile.write(res.content)
            print('done')
