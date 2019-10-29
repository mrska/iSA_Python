# Rysowanie prostokąta o zadanych wymiarach

height = input("Podaj wysokosc prostokata: ")
width = input("Podaj szerokosc prostokata: ")

widthMod = int(width) - 2
heightMod = int(height) - 2

if heightMod < 0 or widthMod < 0:
    print('Nie mozna zbudowac prostokata o podanych wymiarach')
else:
    print("+" + "-" * widthMod + "+ \n" +
          ("|" + " " * widthMod + "| \n") * heightMod +
          "+" + "-" * widthMod + "+ \n")

# Dodac sprawdzenie czy podano liczbe naturalna, ustalic jakies limity
