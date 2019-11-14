# Importowanie modulow
# from - z jakisjs paczki zaimportuj cos
# modul musi byc dostepny w systemie zeby moc go zaimportowac

# camelCase
# snake_case
# kebab-case

# zrobienie modulu - stworzenie pliku i zrobienie na nim modulu
# zeby nie pisac calej sciezki mozemy ustawic kalatog z kodami zrodlowymi i traktowal to jaki najwyzsyz poziom
# modulow mark directories as source root

import lessons.myModule
from lessons.myModule import hello as helloFromModule
# from modules.otherModule import add
#
# # def hello():
# #     print('Dzien dobry')
# # myModule.hello()
# # hello()
# # helloFromModule()
#
# result = add(1, 2, 45, 12)
# print(result)

# Uwtorzyc plik na dysku z wykorzystaniem modulu os
# Przeniesc plik do kosza uzywajac send2trash
# Otworzyc gre saper

# import os
# import send2trash
#
# plik_do_usuniecia = open('plik_do_usuniecia.txt', 'w')
# plik_do_usuniecia.close()
#
# send2trash.send2trash('plik_do_usuniecia.txt')
# os.system('notepad')

# Wysylanie maili
import smtplib # odpowiedzialny za komunikacje, zeby polaczyc sie z serwerem, wyslac maila
from email.mime.text import MIMEText # za przygotoanie pliku w formacie mailowym, teksotwy, krzaczki
from email.mime.multipart import MIMEMultipart

subject = input('Podaj temat')
body = input('Podaj tresc')
recipient = input('Podaj adresata')

mail = MIMEMultipart()
mail["Subject"] = subject
mail["From"] = "isapy@int.pl"
mail["To"] = recipient

mail_body = MIMEText(body) # przerabia tresc maila na cos zrozumiales dla maila
mail.attach(mail_body)


server = smtplib.SMTP("poczta.int.pl")
# wiemy ze nasz serwer potrzebuje uwierzytelniania wiec wlaczamy je:
server.starttls()
server.login(user='isapy@int.pl', password='isapython;')

# jest kilka metod wyslanai
# w send)message wystarczy wkleic to oc mam zdefiniowana
server.send_message(mail)
server.quit()