import gspread
import pprint
import time
import pickle
import shelve
from oauth2client.service_account import ServiceAccountCredentials

link = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']   # задаем ссылку на Гугл таблици
my_creds = ServiceAccountCredentials.from_json_keyfile_name('auth_data.json', link) # формируем данные для входа из json файла
client = gspread.authorize(my_creds)    # запускаем клиент для связи с таблицами
sheet = client.open('graf').sheet1    # открываем нужную на таблицу и лист
day_number = sheet.get_values('A3:AF3')[0]    #считываем номера дней
day_name = sheet.get_values('A4:AF4')[0]    #считываем названия дней
hair1 = sheet.get_values('A5:AF12')        #парикмахерская 1
hair2 = sheet.get_values('A18:AF24')       #парикмахерская 2
hair3 = sheet.get_values('A28:AF33')       #парикмахерская 3
hair4 = sheet.get_values('A38:AF41')       #парикмахерская 4
hair5 = sheet.get_values('A47:AF50')       #парикмахерская 5
calldata = 5                               #создаем переменную, значения которой будут использоваться в calldata бота

def graf_hair(hair):                       #Функция возвращает список из списков графиков работы мастеров парикмахерской
    global count
    graf = []
    for i in hair:                          # i - Строка с имененем мастера и местом его работы или не работы по дням
        graf_m = []                         # Формируем список с именем и графиком работы мастера
        graf_m.append(i[0])                 #Добавляем имя мастера
        l = ''                              #Формируем строку с местом выхода на работу, числом, днем недели
        for j in range(1, len(i)):
            if i[j] != '':                  # Проверяем есть ли запись о выходе на работу в ячейке
                l += i[j] + ' ' + day_name[j] + ' ' + day_number[j] + '\n'      # Добавляем запись о работе, дне, числе
        calldata += 1
        graf_m.append(calldata)
        graf_m.append(l)
        graf.append(graf_m)
    return graf

total_graf = [graf_hair(hair1),graf_hair(hair2),graf_hair(hair3),graf_hair(hair4),graf_hair(hair5)]  #Формируем общий список с графиками работы всех парикмахерских
print(total_graf)

while True:                                                   #Записываем список в файл
    with open("grafic_dump.dat", "wb") as f:
        pickle.dump(total_graf,f)
        time.sleep(36000)
with open("grafic_dump.dat", "rb") as f:
    dic2 = pickle.load(f)
print(dic2)

