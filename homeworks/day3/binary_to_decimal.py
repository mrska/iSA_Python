def binary_to_decimal():
    # Przeliczania licbzy zapisanej w formacie bianarnym na system dziesiętny

    l_binarna = input("Podaj liczbe w formacie binarnym")

    if len(l_binarna.replace("1", "").replace("0", "")) == 0:
        # po usunieciu ze srtinga wszystkich 1 i wszystkich 0 jego dlugosc powinna wynosic 0
        print(int(l_binarna, 2))
    else:
        print('Zly format danych. Podaj liczbe w formacie binarnym')