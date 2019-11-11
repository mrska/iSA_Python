# import csv
#
## Dopisanie nowej linijki do pliku csv
# suma = 0
#
# with open('adresy.csv', 'r+', newline='') as csv_file:
#     csv_data = csv.reader(csv_file)
#
#     for row in csv_data:
#         if row[4].isdigit():
#             suma = suma + int(row[4])
#         print(row)
#
#     print(suma)
#     csv_write = csv.writer(csv_file)
#     csv_write.writerow(['Marta', 'Suska', 'Gdansk', '167181', '26'])

# PICKLE
import pickle
import datetime
import random

entries = [
    {"title": "Pierwszy wpis", "body": "Tresc pierwsza", "author": "Marta", "date": "07.11.2019"},
    {"title": "Drugi wpis", "body": "Tresc druga", "author": "Tomek", "date": "08.11.2019"}
]

def dodajDoKsiazki(tytul, tresc, imie, date):

    with open('book.pkl', 'rb+') as book_file:
        data = pickle.load(book_file)

        entry = {"title": tytul, "body": tresc, "author": imie, "date": date}
        data.append(entry)

        book_file.seek(0) # jakbysmy chcieli znowu zaladowac plik to tez musimy to wywolac zeby ustawic sie na poczatku
        pickle.dump(data, book_file)

def wyswietlKsiazke():
    with open('book.pkl', 'rb') as book_file:
        data = pickle.load(book_file)
        print(data)

def przeszukajKsiazke(szukaj):
    nrId = list()

    with open('book.pkl', 'rb') as book_file:
        data = pickle.load(book_file)
        for i in data:
            for key, value in enumerate(i):
                if szukaj in i[value]:
                    nrId.append(i)
                    break
    if(len(nrId)>0):
        print(nrId)
    else:
        print("Nie znaleziono")

def sortujKsiazke(sortuj, kolejnosc):
    sortujList = list()

    if kolejnosc!='asc' and kolejnosc != 'desc':
        print('Niepoprawnie zdefiniowana kolejnosc. Wpisz asc lub desc ')
    else:

        with open('book.pkl', 'rb') as book_file:
            data = pickle.load(book_file)
            for key, value in enumerate(data):
                if value[sortuj] not in sortujList:
                    sortujList.append(value[sortuj]) # dodajemy tylko unikalne wartosci, zeby potem nie zduplikowac wpisow

            if kolejnosc == 'asc':
                posortowanaKsiazka = sorted(sortujList) # wyrzuci posortowany wynik
            else:
                posortowanaKsiazka = sorted(sortujList, reverse=True)

            for i in posortowanaKsiazka: # dla kazdego wyniku wyrzuci clay slownik w ktorym znajduje sie wynik
                for j in data:
                    if i == j[sortuj]:
                        print(j)

def przegladajKsiazke():
    with open('book.pkl', 'rb') as book_file:
        data = pickle.load(book_file)
        licznik = 0
        print(data[licznik])

        kontynuuj = True
        while kontynuuj == True:
            krok = input('Ktory wpis wyswietlic? Nastepny (N), '
                         'Poprzedni (P), Wyjscie (X) ')
            if krok == 'P':
                if licznik >0:
                    licznik = licznik - 1
                    print(data[licznik])
                else:
                    print('Jestes na poczatku ksiegi gosci')
            elif krok == 'N':
                if licznik < len(data)-1:
                    licznik = licznik + 1
                    print(data[licznik])
                else:
                    print('Jestes na koncu ksiegi gosci')
            elif krok == 'X':
                print('Koniec przegladania wpisow')
                kontynuuj = False
            else:
                print('Niezdefiniownana operacja')

def losujZKsiazki():
    with open('book.pkl', 'rb') as book_file:
        data = pickle.load(book_file)
        id = random.randint(0, len(data)-1)
        print(data[id])

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
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        dodajDoKsiazki(tytul, tresc, imie, date)
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


