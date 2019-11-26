class Zwierze():
    def __init__(self):
        self.oczy = 2
        self.wlosy = True

    def __str__(self):
        return f'Oczy: {self.oczy}, Wlosy: {self.wlosy}'

class Czlowiek(Zwierze):
    def dajglos(self):
        print('Hęę')

    def czy_wlosy(self):
        print('Mam wlosy')

class Dresiarz(Czlowiek):
    def __init__(self):
        super().__init__() # zeby nie zniknely nam oczy, kiedy na nowo definujemy init to zapomina o wszystkich nadrzednych initach
        # super to sposb na odwolanie sie do konstruktora koasy nadrzednej, trzeba to wywolac
        # PRZED tym co zmieniamy. super odwoluje sie do jednego wyzej, a jak nie ma to do kolejnego wyzej
        self.wlosy = False

    def dajglos(self):
        # mozna tu wywolac wszystko np, jesli chcemy sie odwolac do czegos z klasy powyzej
        super().czy_wlosy()
        print('Masz jakis problem?')

class Student(Czlowiek):
    def dajglos(self):
        print('Siema')


class Kot(Zwierze):
    def dajglos(self):
        print('Miau')


class Pies(Zwierze):
    def dajglos(self):
        print('Hau')

class Bokser(Pies):
    pass

class Jamnik(Pies):
    pass

czlowiek = Czlowiek()
zwierze = Zwierze()
pies = Pies()
kot = Kot()
bokser = Bokser()
jamnik = Jamnik()
student = Student()
dresiarz = Dresiarz()

# czlowiek.dajglos()
# pies.dajglos()
# kot.dajglos()
# bokser.dajglos()
# jamnik.dajglos()
# student.dajglos()
# dresiarz.dajglos()

print(dresiarz)
print(student)
print(pies)

dresiarz.dajglos()


class A(object):
    def wypisz(self):
        print("Jestes w A")

class B(A):
    pass
    # def wypisz(self):
    #     print("Jestes w B")

class C(A):
    def wypisz(self):
        print("Jestes w C")

class D(B, C):
    pass

dziecko = D()
dziecko.wypisz()