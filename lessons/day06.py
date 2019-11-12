# import csv
#
## Dopisanie nowej linijki do pliku csv
# suma = 0
#
# with open('adresy.csv', 'r+', newline='') as csv_file:
#     csv_data = csv.reader(csv_file)
#
#     for row in csv_data:
#         if row[4].isdigit():
#             suma = suma + int(row[4])
#         print(row)
#
#     print(suma)
#     csv_write = csv.writer(csv_file)
#     csv_write.writerow(['Marta', 'Suska', 'Gdansk', '167181', '26'])
