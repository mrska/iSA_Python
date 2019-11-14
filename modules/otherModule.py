# spr jak wczytac modul ktory znajduje sie w innym folderze
# w zmiennej args mam krotke ze wszystkimi atrybutami jakie zostaly podane
def add(*args):
    suma = 0
    for i in args:
        if str(i).isdigit():
            suma = suma+i
    return (suma)

    # jesli wiemy ze wszystkie wartosci to liczby
    #return(sum(args))

# magiczne zmienne, w zaleznsoci czy modul wywolywany z tego poziomu czy z importu
# if(__name__ == '__main__'):
#   print('Z poziomu modulu')
# else:
#   print('Z innego poziomu')