# sciaga na dysk wszystkie obrazki do katalogu images - OK
# robi miniaturki z tych obrazow w katalogu images/thumbs o szerokosci 64x 64 - OK
# Policz ile jest zdjec na stronie - OK
# Wyslij maile z informacja iile jest zdjec sciagnietych , sumaryczny rozmiar zdjec w MB
#   ile MB zaoszczedzonych robiac miniaturki
#   i jaka jest pogoda w Gdansku

# zeby od razu zapisac BytesIO
import requests
from bs4 import BeautifulSoup
from PIL import Image
import os

domena = 'https://wallpaperlist.com/'
page = requests.get(domena)
sciezka = r"C:/Users/Marta/Documents/Python/iSA_Python/lessons/images"
sciezka2= r"C:/Users/Marta/Documents/Python/iSA_Python/lessons/images/thumbs"
wallpaper = BeautifulSoup(page.content, 'html.parser')
#
# # Pobieramy obrazki i zapisujemy do katalogu
# for image in wallpaper.find_all('img'):
#
#     adres = domena + image.get("src")
#     tytul =image.get("src").split('/')[-1]
#
#     sciezka_tytul = f"{sciezka}/{tytul}"
#
#     link = requests.get(adres)
#
#     with open(sciezka_tytul, 'wb') as test_file:
#         test_file.write(link.content)


# Zmniejszamy obrazki
lista_obrazkow = os.listdir(sciezka)
liczba_zdjec = 0
rozmiar_zdjec = 0
rozmiar_zdjec2 = 0

for i in lista_obrazkow:
    if(i != 'thumbs'): # jakies madrzejsze rozwiazanie, jak wykluczyc podfoldery z listdir
        image = Image.open(sciezka+'/'+i)
        ratio = image.size[0]/image.size[1]
        image = image.resize((64, int(64/ratio)))
        image.save(sciezka2 + '/' + i )
        liczba_zdjec = liczba_zdjec + 1

        # print(sciezka+'/'+i)
        # print(os.path.getsize(sciezka+'/'+i))
        rozmiar_zdjec = rozmiar_zdjec + os.path.getsize(sciezka+'/'+i)
        rozmiar_zdjec2 = rozmiar_zdjec2 + os.path.getsize(sciezka2+'/'+i)


print(rozmiar_zdjec)
print(rozmiar_zdjec2)








