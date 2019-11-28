import datetime
#
# # zmienne definowane na poziomie klasy
# class Pizza():
#     stawka_vat = 23 # pola klasy
#     __marza = 1.05 # pole prywatne (pole klasy)
#
#     def __init__(self, skladnik_glowny = ''):
#         self.skladnik_glowny = skladnik_glowny
#         self.rozmiar = 30
#         self.ciasto = 'cienkie'
#         self.cena = self.__marza * 100
#
#     @classmethod
#     def Hawajska(cls):
#         return cls('ananas')
#
#     @classmethod
#     def Farmerska(cls):
#         return cls('kielbasa')
#
#     @classmethod
#     def podaj_stawke_vat(cls): # metody klasy, wyniesienie pewnych metod na poziom klasy a nie konkretnego obiektu
#         return cls.stawka_vat # dostep do definicji klasy  za pomoca cls.
#
#     @staticmethod
#     def podaj_date():
#         return datetime.datetime.now().strftime("%Y-%d-%m")
#
#
# hawajska = Pizza('ananas')
# #print(hawajska.skladnik_glowny)
# hawajska = Pizza.Hawajska()
# #print(hawajska.skladnik_glowny)
#
# farmerska = Pizza.Farmerska()
#
# # metody statyczne - nie sa zwiazne ani z obiektem ani z klasa
# np obliczenia matematyczne
# przez self -mozna odwolac sie do wszystkich rzczy zwiazanych z obiektem
# przez cls - do wszystkich pol klasy
# metody statyczne musza miec wszystko podane w parametrze i na tej podstawie cos wypchaja
# w zaden sposob nie dostaniemy sie do danych obiektu, klasy
# print(farmerska.skladnik_glowny)
# print(Pizza.podaj_stawke_vat())
# print(Pizza.stawka_vat) # lepiej sie tak nie odwolywac do pola, tylko zastosowac enkapsulacje i skorzystac z metody
# print(Pizza.podaj_date())
# #print(Pizza.__marza) # nie moge sie do tego dostac tak bo to jest pole prywatne
# # ale moge sie odwolac tak, wiec to jest pseudoprywatne,
# print(Pizza.__dict__) # mowi co w klasie siedzi i co mozna wykonac, wszystko co interpreter moze wykonac
# print(Pizza._Pizza__marza) # teraz wiemy ajkt o zapisac, a tu juz dziala! wystarczy dokelic nazwe klasy
# # tak nie robimy!
# print(Pizza().cena)
# print(Pizza.Farmerska().cena)

class Student():

    def __init__(self):
        self.__imie = None
        self.nazwisko = None
        self.data_dodania = None
        self.data_usuniecia = None
        self.skasowany = False

    @property # wlasciwosci ustawiamy na wlasciwowciach prywatnych
    def imie(self):
        print('org: ' + self.__imie)
        return self.__imie.capitalize()

    @imie.setter
    def imie(self, wartosc):
        self.__imie = wartosc

    @imie.deleter
    def imie(self):
        self.skasowany =  True
        self.data_usuniecia =  self.pobierz_date()

    @staticmethod
    def pobierz_date():
        return datetime.datetime.now().strftime("%Y-%d-%m")


student = Student()
student.imie = 'marta' # to nie zadziala jak prywatne, musze dodac setter i z setterem @imie.setter dzialaS
student.nazwisko = 'Suska'
student.data_dodania = Student.pobierz_date()
print(student.imie)
print(student.nazwisko)
del(student.imie)
print(student.data_dodania)
print(student.data_usuniecia)