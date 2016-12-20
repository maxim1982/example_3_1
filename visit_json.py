import json

with open('visits.json') as read_file:
    countries = json.load(read_file)

# Множества - удобная структура для операций пересечения и объединения, поддерживает уникальность элементов	
# В отличие от списков, элементы множества не упорядочены
schengen_countries = set()
sea_countries = set()
room_rate_countries = set()

money_amount = 40000

for country_name, properties in countries.items():
    if properties[0]['schengen'] == 'True' : # почему то явное указание равенства True  делает проверку
        schengen_countries.add(country_name)

    if properties[0]['sea'] == 'True' : # почему то явное указание равенства True  делает проверку
        sea_countries.add(country_name)

    rent_room_mouth = properties[0]['room_rate'] * 30 # аренда номера
    balance = (money_amount / properties[0]['currency_rate']) - rent_room_mouth
    # проверяем: нам хватит денег прожить там месяц
    if balance >0:
        room_rate_countries.add(country_name)

print ('Страны в шенгене и с морем: %s'% (schengen_countries & sea_countries))

sea_schengen_rent_countries = schengen_countries & sea_countries & room_rate_countries

print('Ответ :')
# Подход со словарем словарей
for country_name in sea_schengen_rent_countries:
    print(country_name,':\n', countries[country_name])

from datetime import datetime
print ('\nУсловия действительны до {:%d-%m-%Y %H:%M}\n'.format(datetime(2017, 6, 15, 23, 59)))