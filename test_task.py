from datetime import datetime, date, time
import random

# Программа, для уведомления клиентов, об истичении срока пользования услугами фитнес клуба.
id_newsletter = random.random() #Переменная рандомного числа, для присвоения индивидуального id номера.
#print(id_newsletter)
num_client = [+79999999999] # Список телефонных номеров клиентов, который необходимо заполнить.

period = datetime.now()
srok = datetime.strptime("04/04/22 12:00", "%d/%m/%y %H:%M") # Взависимости от даты разнятся уведомления.

client = 'id:', id_newsletter, 'н/т:', num_client

if period >= srok:
    print('Клиент {}, время обновить годовой абонемент'.format(client))
else:
    print('Клиент {} доступ к занятиям закрыт'.format(client))



