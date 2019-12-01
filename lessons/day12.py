#locale
import locale
import datetime

locale.setlocale(locale.LC_TIME, 'pl_PL.utf8') # JAK SIE TEGO NIE USTAWI TO BEDZIE PO ANGIELSKU
print(datetime.datetime.now().strftime('%A %B %H:%M:%S'))