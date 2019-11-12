# Zarzadzanie ksiega gosci

from homeworks.day06.KsiegaGosci_func import *

onceAgain = 'T'
while onceAgain == 'T':

    mode = input('Co chcesz zrobic? \ndodac(A), \nwyszukac (S), \nposortowac (O),'
                 ' \nwyswietlic kolejne wpisy (D), \nwyswietlic losowy wpis (R),'
                 '\nwyjsc (X)\n->')
    if mode == 'S': # search
        szukaj = input("Co chcesz wyszukac? ")
        przeszukajKsiazke(szukaj)
        onceAgain = input('Czy chcesz cos jeszcze zrobic? [T/N]: ')

    elif mode == 'A': # add

        tytul = input('Podaj tytul: ')
        tresc = input('Podaj tresc:  ')
        imie = input('Podaj imie: ')

        dodajDoKsiazki(tytul, tresc, imie)
        wyswietlKsiazke()
        onceAgain = input('Czy chcesz cos jeszcze zrobic? [T/N]: ')

    elif mode == 'O': # order
        sortuj = input('Po czym chcesz sortowac. Podaj nazwe kolumny (np date, author): ')
        kolejnosc = input('Rosnaca (asc) czy malejaco (desc)')
        sortujKsiazke(sortuj, kolejnosc)
        onceAgain = input('Czy chcesz cos jeszcze zrobic? [T/N]: ')

    elif mode == 'D': #display
        przegladajKsiazke()
        onceAgain = input('Czy chcesz cos jeszcze zrobic? [T/N]: ')

    elif mode == 'R': # random
        losujZKsiazki()
        onceAgain = input('Czy chcesz cos jeszcze zrobic? [T/N]: ')

    elif mode == 'X':
        print('Do zobaczenia')
        onceAgain = 'N'

    else:
        print('Nie wiem co chcesz zrobic')
        onceAgain = 'T'


# POWROT DO WYJSCIOWYCH DANYCH
# import pickle
#
# entries = [
#     {"title": "Pierwszy wpis", "body": "Tresc pierwsza", "author": "Marta", "date": "07.11.2019"},
#     {"title": "Drugi wpis", "body": "Tresc druga", "author": "Tomek", "date": "08.11.2019"}
# ]
# with open('book.pkl', 'wb') as book_file:
#     pickle.dump(entries, book_file)
