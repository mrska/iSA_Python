# zakaz uzywania input i print
import homeworks.day10.tools as tools
import pickle
import random


class Wpis():
    def __init__(self, title, body, author, data = tools.dzis() ):
        self.author = author
        self.body = body
        self.title = title
        self.date = data

    def tresc(self, dlugosc=None):
        if dlugosc is None:
            return self.body
        else:
            return self.body[:dlugosc] + '...'

    # def utworz_wpis(self):
    # return {"title":f"{self.title}", "body":f"{self.body}", "author":f"{self.author}", "date":f"{self.date}"}
    # BO NIE CHCEMY PRACOWAC NA SLOWNIKACH TYLKO NA OBIEKTACH, W PICKLU SA OBIEKTY!


class Ksiega():
    def __init__(self):
        self.nazwa = 'Ksiega Gosci'
        self.plik = 'book.pkl'
        self.sciezka =r'..\..\lessons\book.pkl'
        self.wpisy = []
        self.__OdczytajKsiazke() # nie bedziemy juz uzywac tych funkcji na zewnattrz, wiec mozemy zrobic  je jako prywatne

    def __OdczytajKsiazke(self):
        try:
            book_file = open(self.sciezka, 'rb+')
            self.wpisy = pickle.load(book_file)
        except: # jesli nie istnieje lub jest pusty
            book_file = open(self.sciezka, 'wb+')

        book_file.close()

    def dodajDoKsiazki(self, wpis): #
        self.wpisy.append(wpis)
        self.__ZapiszDoKsiazki()

    def __ZapiszDoKsiazki(self):
        with open(self.sciezka, 'rb+') as book_file:
            book_file.seek(0)
            pickle.dump(self.wpisy, book_file)

    def PobierzWpisy(self):
        with open(self.sciezka, 'rb') as book_file:
            data = pickle.load(book_file)
            return(data)

    def __len__(self):
        return len(self.wpisy)
    #
    # def przeszukajKsiazke(self, szukaj):
    #     nrId = list()
    #
    #     with open(self.sciezka, 'rb') as book_file:
    #         data = pickle.load(book_file)
    #         for i in data:
    #             for key, value in enumerate(i):
    #                 if szukaj in i[value]:
    #                     nrId.append(i)
    #                     break
    #     if (len(nrId) > 0):
    #         return(nrId)
    #     else:
    #         return('Nie odnaleziono')

    # def sortujKsiazke(self, sortuj, kolejnosc):
    #     sortujList = list()
    #
    #     if kolejnosc != 'asc' and kolejnosc != 'desc':
    #         return('Niepoprawnie zdefiniowana kolejnosc. Wpisz asc lub desc ')
    #     else:
    #
    #         with open(self.sciezka, 'rb') as book_file:
    #             data = pickle.load(book_file)
    #             for key, value in enumerate(data):
    #                 if value[sortuj] not in sortujList:
    #                     sortujList.append(
    #                         value[sortuj])  # dodajemy tylko unikalne wartosci, zeby potem nie zduplikowac wpisow
    #
    #             if kolejnosc == 'asc':
    #                 posortowanaKsiazka = sorted(sortujList)  # wyrzuci posortowany wynik
    #             else:
    #                 posortowanaKsiazka = sorted(sortujList, reverse=True)
    #
    #             for i in posortowanaKsiazka:  # dla kazdego wyniku wyrzuci clay slownik w ktorym znajduje sie wynik
    #                 for j in data:
    #                     if i == j[sortuj]:
    #                         print(j)
    #
    # def przegladajKsiazke(self):
    #     with open(self.sciezka, 'rb') as book_file:
    #         data = pickle.load(book_file)
    #         licznik = 0
    #         print(data[licznik])
    #
    #         kontynuuj = True
    #         while kontynuuj == True:
    #             krok = input('Ktory wpis wyswietlic? Nastepny (N), '
    #                          'Poprzedni (P), Wyjscie (X) ')
    #             if krok == 'P':
    #                 if licznik > 0:
    #                     licznik = licznik - 1
    #                     print(data[licznik])
    #                 else:
    #                     print('Jestes na poczatku ksiegi gosci')
    #             elif krok == 'N':
    #                 if licznik < len(data) - 1:
    #                     licznik = licznik + 1
    #                     print(data[licznik])
    #                 else:
    #                     print('Jestes na koncu ksiegi gosci')
    #             elif krok == 'X':
    #                 print('Koniec przegladania wpisow')
    #                 kontynuuj = False
    #             else:
    #                 print('Niezdefiniownana operacja')
    #
    # def losujZKsiazki(self):
    #     with open(self.sciezka, 'rb') as book_file:
    #         data = pickle.load(book_file)
    #         id = random.randint(0, len(data) - 1)
    #         return(data[id])