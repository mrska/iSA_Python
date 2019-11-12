from lessons.licznikUruchomien import * # na 5 zajeciach tworzylismy program do zliczania uruchomien programu
import string

# Zakladamy ze tekst jest sformatowany poprawnie

def textAnalysis(sciezkaDoTekstu):

    with open(sciezkaDoTekstu, 'r+') as tekst_file:
        tekst_file.seek(0)
        tekst = tekst_file.read()

    # Statystyki:
    liczbaUruchomien = licznikUruchomienFunc('statystykiTekstu_licznik.txt')

    liczbaPrzeanalizowanychZnakow = len(tekst)

    liczbaWyrazow = 0 # Liczba wyrazow = liczba spacji + 1(osttani wyraz po ktorym nie ma juz spacji)
    for i in range(1, len(tekst)):
        if tekst[i] == ' ':
            if i>0 and tekst[i-1] != ' ': # zabezpieczamy sie na wypadek wystapienia podwojnej spacji
                liczbaWyrazow = liczbaWyrazow + 1
    liczbaWyrazow = liczbaWyrazow + 1

    malelitery = list(string.ascii_lowercase)
    duzeLitery = list(string.ascii_uppercase)

    liczbaCyfr = 0
    liczbaMalychLiter = 0
    liczbaDuzychLiter = 0

    for i in tekst:

        if i.isdigit():
                liczbaCyfr = liczbaCyfr + 1

        if i in malelitery:
            liczbaMalychLiter = liczbaMalychLiter + 1

        if i in duzeLitery:
                liczbaDuzychLiter = liczbaDuzychLiter + 1

    liczbaLiter = liczbaMalychLiter + liczbaDuzychLiter

    print(f'Tekst: {sciezkaDoTekstu} \n'
          f'Liczba uruchomien: {liczbaUruchomien} \n'
          f'Liczba przeanalizowanych znakow: {liczbaPrzeanalizowanychZnakow} \n'
          f'Liczba wyrazow: {liczbaWyrazow} \n'
          f'Liczba cyfr: {liczbaCyfr} \n'
          f'Liczba malych liter: {liczbaMalychLiter} \n'
          f'Liczba duzych liter: {liczbaDuzychLiter} \n'
          f'Liczba liter: {liczbaLiter}')

    # Zapisz do pliku ze statystykami
    with open('statystykiTekstu_statystyki.txt', 'r+') as statystyki_file:

        statystyki_file.truncate(0)
        statystyki_file.seek(0)

        statystyki_file.write(f'Tekst: {sciezkaDoTekstu} \n'
                              f'Liczba uruchomien: {liczbaUruchomien} \n'
                              f'Liczba przeanalizowanych znakow: {liczbaPrzeanalizowanychZnakow} \n'
                              f'Liczba wyrazow: {liczbaWyrazow} \n'
                              f'Liczba cyfr: {liczbaCyfr} \n'
                              f'Liczba malych liter: {liczbaMalychLiter} \n'
                              f'Liczba duzych liter: {liczbaDuzychLiter} \n'
                              f'Liczba liter: {liczbaLiter}')




textAnalysis('statystykiTekstu_tekst.txt')

# ilosc uzyc poszczegolnych literek i cyfr
# ilosc zdan
# tryb case sensitivity