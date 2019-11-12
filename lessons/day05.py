# contacts = {"names": ['Ala', 'Ola', 'Jan'],
#             "surnames": ['Kowalska', 'Malinowska', 'Igrekowski'],
#             "cities": ['Gdansk', 'Sopot', 'Gdynia']
#             }
#
# print(contacts)
# print(type(contacts))
# print(contacts['cities'])
# contacts['cities'].append('Warszawa')
# print(contacts)
# contacts.update({'countries': ['Polska', 'USA', 'Szwecja']})
# # to samo co ponizsze
# # ccontacts['countries'] = ['Polska', 'USA', 'Szwecja']
# print(contacts)
# print(len(contacts))
#
# print(contacts.keys())
# print(contacts.items())
# print(list(contacts))
#
# #  Wysiwtelmy
# # "Ala Kowalska mieszka w Gdansk (Polska)"
#
# print('###################################')
# for key, value in enumerate(contacts['names']):
#     string = value +' ' + contacts['surnames'][key] +' mieszka w ' +  contacts['cities'][key] + ' (' +  contacts['countries'][key] + ')'
#     print(string)
#
#
# contacts2 = [
#
#     {"name": "Ala", "surname": "Kowlaska", "cities": "Gdańsk"},
#
#     {"name": "Ola", "surname": "Malinowska", "cities": "USA"},
#
#     {"name": "Jan", "surname": "Igrekowski", "cities": "Dania"}
#
# ]
# print('###################################')
#
# for i in contacts2:
#     print(f"{i['name']} {i['surname']} mieszka w {i['cities']}")
#
#
# contacts3 = {
#
#     '0': {"name": "Ala", "surname": "Kowlaska", "cities": "Gdańsk"},
#
#     '1': {"name": "Ola", "surname": "Malinowska", "cities": "USA"},
#
#     '2': {"name": "Jan", "surname": "Igrekowski", "cities": "Dania"}
#
# }
#
# print('###################################')
#
# for i in contacts3:
#     print(f"{contacts3[i]['name']} {contacts3[i]['surname']} mieszka w {contacts3[i]['cities']}")

# OTWIERANIE PLIKOW
#
# file = open('file.txt', 'w')
# file.write('Zapisz do pliku jeszcze raz')
# file.close()

# with open('file.txt', 'w') as file:
#     print(file.tell())
#     file.write('Zapisz prosze')
#     print(file.tell())
#     file.writelines(['nowa linia\n', 'druga linia\n'])

# Zrobic licznik ueuchomien programu

i = 1
with open('file.txt', 'r+') as file:
    file.seek(0)
    a = file.read()
    # bezpieczniej bedzie z file.truncate(0) wtedy najpierw pobrac, potem wyczyscic potem dodac itd
    file.seek(0)
    file.write(str(int(a)+1))
    print('Uruchomilem sie juz ' + str(int(a)+1))