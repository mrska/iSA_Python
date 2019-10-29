# na podstawie https://pynative.com/python-accept-list-input-from-user/

listaUzytkownika = input("Wpisz elementy listy rozdzielone spacja ")
lista  = listaUzytkownika.split()
dlugoscListy = len(lista)

# ustalenie maksymalnej szerokosc kolumny
szerokosc = 1

licznik = 0
for i in lista:
    if len(i) > 30:
        lista[licznik] = i[0:27] +  "..."
    licznik = licznik + 1

for i in lista:
    if len(i) > szerokosc:
        szerokosc = len(i)

# ustalenie ilosci spacji dla kazdego elementu listy
liczbaSpacji = list()
for i in lista:
    liczbaSpacji.append(szerokosc - len(i))

# dodanie marginesow
szerokosc = szerokosc + 2

linia = ("+" + "-" * szerokosc) * dlugoscListy + "+\n" + "|"
for i in range(0, dlugoscListy):
    linia = linia + " " + lista[i] + liczbaSpacji[i] * " " + " |"

print(linia)




