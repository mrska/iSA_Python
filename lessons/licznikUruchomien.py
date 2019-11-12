def licznikUruchomienFunc(sciezkaDoPlikuTxt):
    i = 1
    with open(sciezkaDoPlikuTxt, 'r+') as file:
        file.seek(0)
        data = file.read()
        file.truncate(0)
        file.seek(0)
        file.write(str(int(data)+1))
        #print('Uruchomilem sie juz ' + str(int(data)+1))
    return(int(data)+1)