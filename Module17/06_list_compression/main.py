import random

n = int(input('Кол-во чисел в списке: '))

num_list = list([random.randint(0, 2) for _ in range(n)])
print('Список до сжатия:', num_list)

new_num_list = list([x for x in num_list if x != 0])
print('Список после сжатия:', new_num_list)
