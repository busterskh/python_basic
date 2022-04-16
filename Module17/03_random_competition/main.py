import random
first_command = list([round(random.uniform(5.00, 10.00), 2) for _ in range(20)])
second_command = list([round(random.uniform(5.00, 10.00), 2) for _ in range(20)])
winner_list = list([max(first_command[x], second_command[x]) for x in range(20)])

print('Первая команда:', first_command)
print('Вторая команда:', second_command)
print('Победители тура:', winner_list)
