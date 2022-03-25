def count_number(n):
    count = 0
    for num in str(n):
        count += 1
    print('Кол-во цифр в числе:', count)
    return count


def summ_number(n):
    summ = 0
    while n != 0:
        summ += n % 10
        n //= 10
    print('Сумма цифр:', summ)
    return summ


n = int(input('Введите число: '))
result = summ_number(n) - count_number(n)

print('Разность суммы и кол-ва цифр:', result)
