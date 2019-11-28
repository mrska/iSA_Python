from homeworks.day10.KsiegaGosciModel import Wpis
from homeworks.day10.KsiegaGosciModel import Ksiega
import homeworks.day10.KsiegaGosciView as View

View.menu()
opcja = input('Moj wybór:')
 # kontroler ma zwykle duzo ifów

ksiega = Ksiega()
if opcja == 'A': # search
    author = input('Jak masz na imie: ')
    body = input('Podaj tresc: ')
    title = input('Podaj tytul wpisu: ')

    wpis = Wpis(title, body, author)
    ksiega.dodajDoKsiazki(wpis)
    rozmiar = len(ksiega)
    View.pokaz_rozmiar(rozmiar)
elif opcja == 'P':
   wszystkieWpisy = ksiega.PobierzWpisy()
   View.pokaz_wpisy(wszystkieWpisy)
else:
    View.blad()
