# debuging
# days = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
# weekend = ('sobota', 'niedziela')
#
# for day in days:
#     if day in weekend:
#         print('Jest weekend')
#     else:
#         print('Nie ma weekendu')

# operacja na obrazach
# from PIL import Image
#
# image = Image.open(r'owl.jpg')
# # image: Image.Image = Image.open(r'owl.jpg')) # po to zeby pomoc podpowiadac, ulatwienie
# #image.show()
#
# image = image.rotate(90)
# image = image.resize((1000, 1000))
# image.save('owl2.jpg')

# requesty
# import requests
# api_host = 'http://api.openweathermap.org/data/2.5/weather'
# api_key = '800101cc05e0bcd5b88c816246c988ff'
# city = 'Gdansk'
#
# weather_city = requests.get(f'{api_host}?appid={api_key}&q={city}')
# dict = weather_city.json()
#
# # dobrze uruchomic to w debugerze, wtedy lepiej wyswietla sie slownik
# # klikamy evaluate i wiemy jak to wysiwtelic
# print(f"temperatura: {dict['main']['temp']}")
# print(f"wiatr {dict['wind']['speed']}")

#
#from bs4 import BeautifulSoup

# przyklady uzywania
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.get_text())
#
# for link in soup.find_all('a'):
#     print(link.get('href'))

# z podanej strony https://wallpaperlist.com/
# chcemy pobrac wszystkie obrazki

import requests
from bs4 import BeautifulSoup

domena = 'https://wallpaperlist.com/'
page = requests.get(domena)
#print(page.content)

wallpaper = BeautifulSoup(page.content, 'html.parser')

for image in wallpaper.find_all('img'):
    #print(image.get("src")) # te linki sa wzgledne, wystarczy dokleic do domeny i mamy foto
    print(domena + image.get("src"))
    #print(image['src']) # dziala tak samo
