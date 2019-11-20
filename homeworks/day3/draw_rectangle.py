def draw_rectangle():
    # Rysowanie prostokąta o zadanych wymiarach

    height = input("Podaj wysokosc prostokata: ")
    width = input("Podaj szerokosc prostokata: ")

    if height.isdigit() and width.isdigit():

        widthMod = int(width) - 2
        heightMod = int(height) - 2

        if heightMod > 198 or widthMod>198:
            print("Troche Cie ponioslo z tymi wymiarami. Max wymiar 200x200")
        else:

            print("+" + "-" * widthMod + "+ \n" +
                  ("|" + " " * widthMod + "| \n") * heightMod +
                  "+" + "-" * widthMod + "+ \n")
    else:
        print('Zly format danych. Podaj liczby naturalne')