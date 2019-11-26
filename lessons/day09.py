# definijemy klase
class Krzeslo(): # klasa musi miec konstruktor
    def __init__(self, kolor_siedziska = 'czerwony', cena = 100):
        #print('Tworze obiekt') # ale printow nie robimy w klasach, model mvc, jak nie mieszac, czemu nie robic printow w funkcjach i w klasach
        self.kolor_siedziska = kolor_siedziska # nasz obiekt krzesla ma jakies wlasciwiosci, musimy je zakodowac
        self.ilosc_kol = 5 # teraz mozna sie do tych wszytskich wlasciwiosci odwolac po kropce
        self.ilosc_nog = 5
        self.wysokosc = 90
        self.szerokosc = 40
        self.glebokosc = 40
        self.regulacja_wysokosci = True
        self.regulacja_podlokietnikow = False
        self.material = '100% cotton'
        self.cena = cena
        self.vat = 23

    def __str__(self): # wywoluje sie wtedy kiedy nasz program poprosi o reprezentacje graficzna naszegoobiektu, co ma wyswitlic np print
        return f'Krzeslo koloru: {self.kolor_siedziska}'

    def __len__(self):
        return self.wysokosc * self.szerokosc * self.glebokosc

    def pobierz_cene_netto(self): # lepiej zrobic metoda jak chcemy cene niz robic obiekt.cena
        return self.cena

    def pobierz_cene_brutto(self):
        return self.cena * (1 + self.vat/100)

class Stol():
    def __init__(self):
        self.ilosc_nog = 4

    def __add__(self, other):
        return self.ilosc_nog + other.ilosc_nog
# musimy wiedziec jakiej klasy obiekt chce stworzyc

# tworzymy kilka roznych krzesel
obiekt = Krzeslo('zielony')
#print(obiekt) # kazdy ma inny adres
print(obiekt)
print(obiekt.kolor_siedziska)

obiekt = Krzeslo()
print(obiekt)
print(obiekt.kolor_siedziska)

print(len(obiekt)) # wywolywane w konteksie funkcji, a nie przez kropke
obiekt = Krzeslo('zielona', 120)
print(obiekt)
print(obiekt.kolor_siedziska)

obiekt = Krzeslo()
print(obiekt.pobierz_cene_netto())
print(obiekt.pobierz_cene_brutto())

obiekt2 = Krzeslo('zielona', 120)
print(obiekt2.pobierz_cene_netto())
# mozna sie tez odwolac bezporendio do warosci - hermetyzacja
print(obiekt2.cena) # niebezpieczne, jak z tego bedziemy chcieli policzyc brutto i na sztywno wpiszemy * 1.23 a zmieni sie
# vat, to mamy problem
print(obiekt2.pobierz_cene_brutto())
# Metody sa zdefiniowane w klasach
# Funkcje sa osobnymi bytami

krzeslo  = Krzeslo()
stol = Stol()

print(krzeslo)
print(stol)
print(stol+krzeslo)

