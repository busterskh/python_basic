count_number = int(input('Введите длину списка:'))
number_list = list([x % 5 if x % 2 != 0 else 1 for x in range(count_number)])
print(number_list)