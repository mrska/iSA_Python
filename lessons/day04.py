# Referencje
# lista = [1, 2, 3]
# nowa_lista = lista
#
# # stworzenie faktycznej kopii
# #kopia_listy = lista.copy()
# kopia_listy = lista[:] # slicing, bierze od pierwszego do ostatniego i kopiuje
#
# lista[0] = 6
# # mimo ze zmieniamy tylko liste pierwotna, to nowa lista tez bedzie zmieniona
# # nowa_lista to tylko odwolanie do pamieci
#
# print(lista)
# print(nowa_lista)
# print(kopia_listy)

# import copy # potrzebne do glebokiej kopii
#
# # przyklad z listami zagniezdzonymi
# lista = [1,
#          2,
#          3,
#          ["A", "B", "C"]]
#
# nowa_lista= lista
# kopia_listy = lista.copy() # lista zagniezdzona dalej jest referencja
# # zeby wszystko bylo kopia
# gleboka_kopia_listy = copy.deepcopy(lista)
#
# lista[0] = 'X'
# lista[3][0] = 'Y'
#
# print(lista)
# print(nowa_lista)
# print(kopia_listy)
# print(gleboka_kopia_listy)

# FUKCJE

# def do_nothing():
#     pass
#
# do_nothing()
# wynik = do_nothing
# wynik()

# def witaj():
#     print('Witaj')
#
# witaj()
# hi = witaj()
# print(hi)

# def do_nothing(x, y, imie = "Ola", wiek = 22):
#     pass
#
# do_nothing(1, 2, imie = 'Pola', wiek = 98)

imie = "Jola"
def zmien_imie():
    imie = "Teresa"
    return imie

print(imie)
imie = zmien_imie()
print(imie)