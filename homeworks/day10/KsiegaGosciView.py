# tu printy
def menu():
    print('Witaj w ksiedze gosci. Wybierz opcje:')
    print('Co chcesz zrobic? \ndodac(A), \nwyszukac (S), \nposortowac (O),'
                 ' \nwyswietlic kolejne wpisy (D), \nwyswietlic losowy wpis (R), \nwyswietlic cala ksiazke (P)' 
                 '\nwyjsc (X)\n->')

def blad():
    print('Wystapil blad')

def pokaz_rozmiar(rozmiar):
    print(f'Twoja ksiega ma rozmiar {rozmiar}')

def pokaz_wpisy(wpisy):
    for wpis in wpisy:
        print('-'*20)
        print(f'Autor: {wpis.author}')
        print(f'Tresc: {wpis.tresc()}')
        print(f'Tresc skrocona: {wpis.tresc(3)}') # robimy z tresci gettera, na razie metode potem gettera
        print(f'Tytul: {wpis.title}')

