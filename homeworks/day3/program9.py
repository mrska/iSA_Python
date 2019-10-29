# Kalkulator do wyliczenia wieku psa

lataLudzkie = int(input("Podaj wiek psa w latach ludzkich: "))

if lataLudzkie >= 2:
    lataPsie = 10.5 * 2 + (lataLudzkie-2)*4
else:
    lataPsie = 10.5 * lataLudzkie

print(f"Wiek psa w latach psich wynosi {lataPsie}")
