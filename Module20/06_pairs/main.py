import random

number_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', number_list)

new_number_list = [tuple(number_list[i:i + 2]) for i in range(0, 10, 2)]

print('Новый список:', new_number_list)



