# PROGRAM NAKLADKA

from homeworks.day3.multirun import *
from homeworks.day3.celsius_fahrenheit import *
from homeworks.day3.edge_values import *
from homeworks.day3.draw_rectangle import *
from homeworks.day3.binary_to_decimal import *
from homeworks.day3.check_leap_year import *

menu = [["1", "Przeliczenie stopni Celsjusza na Fahrenheita i odwrotnie", celsius_fahrenheit],
        ["2", "Wyznaczenie pierwszej i ostatniej cyfry podanej liczby", edge_values],
        ["3", "Narysowanie prostokąta o zadanych wymiarach", draw_rectangle],
        ["4", "Przeliczenie liczby zapisanej w formacie binarnym na system dziesietny", binary_to_decimal],
        ["5", "Sprawdzenie, czy podany rok jest rokiem przestepnym", check_leap_year],
        # ["6", "Wyswietlanie listy w postaci tabeli"],
        # ["7", "Rozmienianie danej kwoty"],
        # ["8", "Rysowanie piramidy"],
        # ["9", "Wyliczanie wieku psa"],
        # ["10", "Formatowanie tekstu"],
        # ["R", "Wybierz program losowo"],
        ["Q", "Wyjscie"]
        ]

print('Wybierz program:')
for i in range(0, len(menu)):
    print(') '.join(menu[i][0:2]))

innyProgram = "Y"
while innyProgram == "Y":
    wybor = input('Twoj wybor:')

    print('#######################################################################')

    for i in menu:

        if wybor == i[0]:
            twoj_wybor = i
            break
    print(') '.join(twoj_wybor[0:2]))
    if twoj_wybor[0] == 'Q':
        innyProgram = "N"
        print('Do zobaczenia')
    else:
        multirun(twoj_wybor[2])
        innyProgram = input('Czy chcesz wybrac inny program [Y/N]')

    print('#######################################################################')




