# Wyliczenie jak rozmienic podana kwote na monety

kwota = float(input("Podaj kwotę: "))

kwota = kwota * 100
reszta = kwota
moneta = 500

print("Podana kwote mozna rozmienic za pomoca: ")
while reszta != 0:

    iloscMonet = kwota // moneta
    reszta = kwota % moneta

    if iloscMonet != 0:
        print(f"{iloscMonet} monet o wartości {moneta/100}")

    if moneta >= 200:
        moneta = round(moneta/200) * 100
    else:
        moneta = round(moneta/200, 1) * 100
    kwota = reszta
