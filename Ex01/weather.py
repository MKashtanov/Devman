import requests

def getWeather(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

listUrl = ['https://wttr.in/london?nTqu&lang=en',
    'https://wttr.in/svo?nTqM&lang=ru',
    'https://wttr.in/%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D0%B5%D1%86?nTqM&lang=ru'
    ]

for url in listUrl:
    print(getWeather(url))