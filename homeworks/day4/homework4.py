# FUNKCJE POMOCNICZE
def check_float(inputValue):
    # Sprawdzanie czy podana zostala liczba
    try:
        value = float(inputValue)
        status = 'success'
    except ValueError:
        print('Zly format danych. Wprowadz liczbe')
        status = 'fail'

    return(status)

def multirun(funkcja, toRepeat = "Y"):
    # Czy uruchomic program jeszcze raz
    while toRepeat == "Y":
        funkcja()
        toRepeat = input("Czy powtorzyc? [Y/N]")

#######################################################################
#######################################################################
#######################################################################
#######################################################################

# FUNKCJE WŁASCIWE
def celsius_fahrenheit():
    # Przeliczanie stopni Celsjusza na Fahrenheita i odwrotnie

        scale = input("Celsjusz czy Fahrenheit? [C/F] ").upper()

        if scale != "C" and scale != "F":
            print('Nieobslugiwany rodzaj skali.')
        else:
            tempOrg = input("Podaj stopnie: ")

            status = check_float(tempOrg)
            if status == 'success':

                tempOrg = float(tempOrg)

                if scale == "C":
                    print("Skorzystamy ze wzoru: tempF = 9/5 * tempC + 32")
                    part1 = 9 / 5 * tempOrg
                    print("9/5 * " + str(tempOrg) + " = " + str(part1))
                    part2 = part1 + 32
                    print(str(part1) + " + 32 = " + str(part2) + " F")
                else:
                    print("Skorzystamy ze wzoru: tempC = 5/9 * (tempF - 32)")
                    part1 = tempOrg - 32
                    print(str(tempOrg) + " - 32 = " + str(part1))
                    part2 = 5 / 9 * part1
                    print("5/9 * " + str(part1) + " = " + str(part2) + " C")

def edge_values():

    number = input("Podaj liczbę: ")

    status = check_float(number)
    if status == 'success':

        if '-' in number:
            number = number[1:]
        print("Pierwsza cyfra liczby " + number + " to " + number[0] + "\n" +
              "Ostatnia cyfra liczby " + number + " to " + number[-1])

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

def binary_to_decimal():
    # Przeliczania licbzy zapisanej w formacie bianarnym na system dziesiętny

    l_binarna = input("Podaj liczbe w formacie binarnym")

    if len(l_binarna.replace("1", "").replace("0", "")) == 0:
        # po usunieciu ze srtinga wszystkich 1 i wszystkich 0 jego dlugosc powinna wynosic 0
        print(int(l_binarna, 2))
    else:
        print('Zly format danych. Podaj liczbe w formacie binarnym')

def check_leap_year():
    # Sprawdzanie, czy podany rok jest rokiem przestępnym

    rok = input("Podaj rok: ")

    if rok.isdigit():
        rok = int(rok)
        if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
            print("Rok " + str(rok) + " jest rokiem przestępnym")
        else:
            print("Rok " + str(rok) + " nie jest rokiem przestępnym")
    else:
        print('Zly format danych. Podaj liczbe naturalna')

# przyklad uzycia
#multirun(check_leap_year)

#######################################################################
#######################################################################
#######################################################################
#######################################################################

