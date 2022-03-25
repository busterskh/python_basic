def lcd(n):
    for x in range(2, n + 1):
        if n % x == 0:
            break
    print('Наименьший делитель, отличный от единицы:', x)


n = int(input('Введите число: '))
while n < 1:
    n = int(input('Введите число больше чем 1: '))
lcd(n)