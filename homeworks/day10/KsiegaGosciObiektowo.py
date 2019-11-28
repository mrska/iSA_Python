import datetime
import pickle
import pprint
import random

class Wpis():
    def __init__(self, title, body, author):
        self.author = author
        self.body = body
        self.title = title
        self.date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def utworz_wpis(self):
        return {"title":f"{self.title}", "body":f"{self.body}", "author":f"{self.author}", "date":f"{self.date}"}

class Ksiega():
    def __init__(self):
        self.sciezka =r'..\..\lessons\book.pkl'

    def dodajDoKsiazki(self, wpis):
        with open(self.sciezka, 'rb+') as book_file:
            data = pickle.load(book_file)

            entry =wpis
            data.append(entry)

            book_file.seek(0)
            pickle.dump(data, book_file)
            print('Dodano') # do usuniecia

    def wyswietlKsiazke(self):
        with open(self.sciezka, 'rb') as book_file:
            data = pickle.load(book_file)
            pprint.pprint(data)

    def przeszukajKsiazke(self, szukaj):
        nrId = list()

        with open(self.sciezka, 'rb') as book_file:
            data = pickle.load(book_file)
            for i in data:
                for key, value in enumerate(i):
                    if szukaj in i[value]:
                        nrId.append(i)
                        break
        if (len(nrId) > 0):
            pprint.pprint(nrId)
        else:
            print("Nie znaleziono")

    def sortujKsiazke(self, sortuj, kolejnosc):
        sortujList = list()

        if kolejnosc != 'asc' and kolejnosc != 'desc':
            print('Niepoprawnie zdefiniowana kolejnosc. Wpisz asc lub desc ')
        else:

            with open(self.sciezka, 'rb') as book_file:
                data = pickle.load(book_file)
                for key, value in enumerate(data):
                    if value[sortuj] not in sortujList:
                        sortujList.append(
                            value[sortuj])  # dodajemy tylko unikalne wartosci, zeby potem nie zduplikowac wpisow

                if kolejnosc == 'asc':
                    posortowanaKsiazka = sorted(sortujList)  # wyrzuci posortowany wynik
                else:
                    posortowanaKsiazka = sorted(sortujList, reverse=True)

                for i in posortowanaKsiazka:  # dla kazdego wyniku wyrzuci clay slownik w ktorym znajduje sie wynik
                    for j in data:
                        if i == j[sortuj]:
                            print(j)

    def przegladajKsiazke(self):
        with open(self.sciezka, 'rb') as book_file:
            data = pickle.load(book_file)
            licznik = 0
            print(data[licznik])

            kontynuuj = True
            while kontynuuj == True:
                krok = input('Ktory wpis wyswietlic? Nastepny (N), '
                             'Poprzedni (P), Wyjscie (X) ')
                if krok == 'P':
                    if licznik > 0:
                        licznik = licznik - 1
                        print(data[licznik])
                    else:
                        print('Jestes na poczatku ksiegi gosci')
                elif krok == 'N':
                    if licznik < len(data) - 1:
                        licznik = licznik + 1
                        print(data[licznik])
                    else:
                        print('Jestes na koncu ksiegi gosci')
                elif krok == 'X':
                    print('Koniec przegladania wpisow')
                    kontynuuj = False
                else:
                    print('Niezdefiniownana operacja')

    def losujZKsiazki(self):
        with open(self.sciezka, 'rb') as book_file:
            data = pickle.load(book_file)
            id = random.randint(0, len(data) - 1)
            print(data[id])

#NowyWpis = Wpis('tescik', 'tres2', 'MS').utworz_wpis()
Ksiega().przegladajKsiazke()