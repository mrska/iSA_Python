# Przetworzenie danych dot temperatury

def convert_string():
    dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

    start = 0
    end = 4
    for i in range(0, 24):

        wynik = float(dane[start:end-2] + "." + dane[end-2:end])

        if i < 10:
            godzina = f"0{i}:00"
        else:
            godzina = f"{i}:00"

        if wynik <= 18.5:
            znacznik = "\t!!"
        elif wynik > 20:
            znacznik = ""
        else:
            znacznik = "\t!"

        print(f"{godzina}\t%0.2f\u00b0C{znacznik}"%wynik)

        start = start + 4
        end = end + 4
