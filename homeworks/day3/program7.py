# Wyliczenie jak rozmienic podana kwote na monety

kwota = float(input("Podaj kwotę: "))

# Operujemy na groszach
kwota = kwota * 100
reszta = kwota
moneta = 500  # zaczynamy od 5zl

print("Podana kwote mozna rozmienic za pomoca: ")
while reszta != 0:

    iloscMonet = kwota // moneta
    reszta = kwota % moneta

    if iloscMonet != 0:
        print(f"{iloscMonet} monet o wartości {moneta/100}")

    # przejscia do kolejnych nominalow w kolejnych iteracjach
    # 5zl -> 2zl: 200 gr = round(500gr/ 200)
    # 2zl -> 1zl: 100 gr = round(200gr/200)

    # 1zl -> 0.5zl: 50gr = round(100gr/200, 1) # jesli moneta <200gr musimy uwzgledniac pierwsze miejsce po przecinku
    # 0.5zl -> 0.2zl: 20gr = round(50gr/200, 1)
    # 0.2zl -> 0.1zl: 10gr = round(20gr/200, 1)

    if moneta >= 200:
        moneta = round(moneta/200) * 100
    else:
        moneta = round(moneta/200, 1) * 100
    kwota = reszta
