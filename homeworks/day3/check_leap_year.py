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