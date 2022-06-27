import re

numbers = r'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

civil_pattern = r'[АВЕКМНОРСТУХ]\d{3}\w{2}\d{3}'
taxi_pattern = r'[АВЕКМНОРСТУХ]{2}\d{5,6}'

target_number = re.findall(civil_pattern, numbers)
taxi_number = re.findall(taxi_pattern, numbers)

print(f'Список номеров частных автомобилей: {target_number}')
print(f'Список номеров такси: {taxi_number}')

