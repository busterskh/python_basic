string = input('Строка: ')
number_tuple = input('Кортеж чисел: ').split(', ')

zip_result = []
for i_str in string:
    zip_tuple = (i_str, int(number_tuple[0]))
    zip_result.append(zip_tuple)
    number_tuple.pop(0)

for i in enumerate(zip_result):
    print(i[1])
