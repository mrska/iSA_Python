# Rysowanie piramidy o zadanej wysokości

def pyramid_height():
    wysokoscPiramidy  = int(input("Podaj wysokość piramidy: "))

    for i in range(0, wysokoscPiramidy):
        print((wysokoscPiramidy - i - 1) * " " + (i * 2 + 1) * "#" + (wysokoscPiramidy - i - 1) * " ")