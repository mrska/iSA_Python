# Rysowanie piramidy o zadanej wysokości

wysokoscPiramidy  = int(input("Podaj wysokość piramidy: "))

for i in range(0, wysokoscPiramidy):
    print((wysokoscPiramidy - i - 1) * " " + (i * 2 + 1) * "#" + (wysokoscPiramidy - i - 1) * " ")