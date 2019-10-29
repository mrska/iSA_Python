# Przeliczania licbzy zapisanej w formacie bianarnym na system dziesiętny

l_binarna = input("Podaj liczbe w formacie binarnym")

l_binarna_rev = l_binarna[::-1]

l_binarna_len = range(0, len(l_binarna_rev))

l_dziesietna = 0
for i in l_binarna_len:
    l_dziesietna = l_dziesietna + int(l_binarna_rev[i]) * (2 ** i)

print(l_dziesietna)

# dodac sprawdzenie czy liczba jest w formacie binarnym
