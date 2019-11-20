def multirun(funkcja, toRepeat = "Y"):
    # Czy uruchomic program jeszcze raz
    while toRepeat == "Y":
        funkcja()
        toRepeat = input("Czy powtorzyc? [Y/N]")