from homeworks.day3.check_float import *

def edge_values():

    number = input("Podaj liczbę: ")

    status = check_float(number)
    if status == 'success':

        if '-' in number:
            number = number[1:]
        print("Pierwsza cyfra liczby " + number + " to " + number[0] + "\n" +
              "Ostatnia cyfra liczby " + number + " to " + number[-1])