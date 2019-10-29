#wiek = input("Ile masz lat?")
#zwierzaki = input("Ile masz zwierzakow?")

#zdanie = "Ala ma 2 lata i posiada 5 kotow"

# dla typu int by nie dzialalo
#zdanie = "Ala ma " + wiek + " lata i posiada " + zwierzaki + " kotow"
# inny spposob
#zdanie = f"Ala ma {wiek} lata i posiada {zwierzaki} kotow"
#zdanie = "Ala ma {} lata i posiada {} kotow".format(wiek, zwierzaki)
#zdanie = "Ala ma {a} lata i posiada {b} kotow".format(a = wiek, b = zwierzaki)

# TYLKO DO WYSWIETLANIA
# liczba = 1.299
# # print("liczba: %s" %liczba)
# # print("liczba: %0.1f" %liczba) # mozna podac dokladna wartosc
# # print("liczba: %d" %liczba)
# #
# # # INDEKSOWANIE
# # zdanie = "encyklopedia"
# # print(zdanie[::-1]) # najprostszy sposob na odwrocenie stringa


# INSTRUKCJE WARUNKOWE
# zmienna = int(input("Podaj liczbe: "))
#
# if zmienna % 3 == 0 and zmienna % 5 == 0:
#     print("Liczba {} jest podzielna przez 3 i przez 5".format(zmienna))
# elif zmienna % 3 == 0:
#     print("Liczba {} jest podzielna przez 3 i nie jest podzielna przez 5".format(zmienna))
# elif zmienna % 5 == 0:
#     print("Liczba {} jest podzielna przez 5 i nie jest podzielna przez 3".format(zmienna))
# else:
#     print(f"Liczba {zmienna} nie jest podzielna ani przez 3 ani przez 5")


# RANGE LIST TUPLE
# wyrazy = ('raz', 'dwa', 'trzy')
# wyrazy[0] = 'jeden' # wyrzuci blad, bo krotki nie mozna modyfikowac
# print(wyrazy)

# wyrazy = ['raz', 'dwa', 'trzy']
# wyrazy[0] = 'jeden'
# print(wyrazy)

# liczby_parzyste = range(0, 20, 2)
# print(liczby_parzyste)
# if 10 in liczby_parzyste:
#     print('parzysta')
#
# # jesli chcemy zobaczyc te liczby, czyli dodac te liczby do pamieci, to musmy zrobic z tego liste
# lista_liczba_parzystych = list(range(0, 20, 2))
# print(lista_liczba_parzystych)
#
# lista_liczba_parzystych = tuple(range(0, 20, 2))
# print(lista_liczba_parzystych)
#
# lista5 = ["dwa"]
# lista6 = list("dwa")
# print(lista5)
# print(lista6)

#lista6 = list(1) # To nie jest iterowalne wiec nie zadziala

# Lista zakupow
#zakupy = ["kielbasa", "piwko", "chipsy", "wegiel", "kubeczki"]
# zakupy.append("talerzyki")
# zakupy.insert(0, "grill") # wstawi na okreslonym miejscu, nie zastapi, tylko doda na danej pozycji
# zakupy[0] = "elektryczny grill"
# zakupy.remove("piwko")
#
# if("vodka" in zakupy):
#     zakupy.remove("vodka") # jesli nie byloby vodki, to wyrzucilby blad
# # del(zakupy[0]) # tak tez mozna usunac jakis element
#
# zakupy.sort()
# print(zakupy)

# lista = (
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# )
#
# lista[1][2]= [5,6,6] # nie mozna podyfikowac elementow krotki, ale mozna modyfikowac elementy elementow krotki
# print(lista)

# PETLA WHILE

# print("Start")
# zapytaj_ponownie = "T"
# while zapytaj_ponownie == "T":
#     zapytaj_ponownie_org = input("Czy zapytac ponownie [T/N]? :")
#     zapytaj_ponownie = zapytaj_ponownie_org.upper()
#     print(f"odpowiedziales {zapytaj_ponownie_org}")
#
# print("Koniec")

# PETLA FOR

zakupy = ["kielbasa", "piwko", "chipsy", "wegiel", "kubeczki"]

for przedmiot in zakupy:
    if przedmiot == 'piwko':
        znak = '[x] '
    else:
        znak = '[ ] '
    print(znak +  przedmiot)

for litera in "jakies zdanie":
    print(litera)