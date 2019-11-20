from homeworks.day3.check_float import *

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