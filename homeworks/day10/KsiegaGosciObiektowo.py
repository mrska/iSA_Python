import datetime
import pickle

class Wpis():
    def __init__(self, title, body, author):
        self.author = author
        self.body = body
        self.title = title
        self.date =  datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def utworz_wpis(self):
        return {"title":f"{self.title}", "body":f"{self.body}", "author":f"{self.author}", "date":f"{self.date}"}

class Ksiega():
    def __init__(self, wpis):
        self.sciezka =r'..\..\lessons\book.pkl'
        self.wpis = wpis


    def dodaj_wpis(self):
        with open(self.sciezka, 'rb+') as book_file:
            data = pickle.load(book_file)

            entry =self.wpis
            data.append(entry)

            book_file.seek(0)
            pickle.dump(data, book_file)
            print('Dodano')

NowyWpis = Wpis('tytul', 'body', 'Marta').utworz_wpis()
Ksiega(NowyWpis).dodaj_wpis()
