# na podstawie https://pynative.com/python-accept-list-input-from-user/

def list_as_table():
    listaUzytkownika = input("Wpisz elementy listy rozdzielone spacja, a listy zagnieżdżone rozdzielone \'-\' ")  # np aaaa-a a-b-c aa1  1-2
    lista1  = listaUzytkownika.split()
    lista2 = list()

    for i in range(0,len(lista1)):
       listaTemp = lista1[i].split("-")
       lista2.append(listaTemp)

    # ustalenie liczby wierszy
    liczbaWierszy = len(lista2)

    # ustalenie liczby kolumn
    liczbaKolumn = 0
    for i in lista2:
        szerokoscTemp = len(i)
        if szerokoscTemp > liczbaKolumn:
            liczbaKolumn = szerokoscTemp

    # dopisanie elementow do krotszych list
    for i in range(0, len(lista2)):
        szerokoscTemp = len(lista2[i])
        while szerokoscTemp < liczbaKolumn:
            lista2[i].append("")
            szerokoscTemp = len(lista2[i])
    # ustalenie maksymalnej szerokosc kolumny
    szerokoscKolumn = 1
    for i in range(0, len(lista2)):
        for j in range(0, len(lista2[i])):
            if len(lista2[i][j]) > 30:
                lista2[i][j] = lista2[i][j][0:27] + "..."

            szerokosc = len(lista2[i][j])

            if szerokosc > szerokoscKolumn:
                szerokoscKolumn = szerokosc

    # dodanie spacji, zeby kazd akolumna byla tej samej szerokosci
    liczbaSpacji = list()
    for i in range(0, len(lista2)):
        for j in range(0, len(lista2[i])):
            while szerokoscKolumn > len(lista2[i][j]):
                lista2[i][j] = lista2[i][j]+' '

    #dodanie marginesow
    szerokoscKolumn = szerokoscKolumn + 2

    linia = ""
    licznik = 0
    for i in range(0, len(lista2)):
        linia = linia + ("+" + "-" * szerokoscKolumn) * liczbaKolumn + "+\n"
        for j in range(0, len(lista2[i])):
            linia = linia + "| " + lista2[i][j] + " "
        linia = linia + "|\n"

    linia = linia + ("+" + "-" * szerokoscKolumn) * liczbaKolumn + "+\n"

    print(linia)
