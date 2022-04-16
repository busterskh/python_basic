import random

sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))
sticks = list('I' for _ in range(sticks))

for i_throws in range(throws):
    L_i = random.randint(0, 8)
    R_i = random.randint(L_i + 1, 9)
    print(f'Бросок {i_throws + 1}. Сбиты палки с номера {L_i + 1} по номер {R_i + 1}')
    sticks[L_i:R_i + 1] = ['.'] * (R_i + 1 - L_i)

print('Результат:', end=' ')
for x in sticks:
    print(x, end='')
