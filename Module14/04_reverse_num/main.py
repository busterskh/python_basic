def turn_number(number):
    int_number_turn = ''
    float_number_turn = ''
    for n in number:
        if n == '.':
            break
        else:
            int_number_turn = n + int_number_turn
    for x in number[::-1]:
        if x == '.':
            break
        else:
            float_number_turn += x
    result = int_number_turn + '.' + float_number_turn
    return result


n = input('Введите первое число: ')
k = input('Введите второе число: ')

n = turn_number(n)
print('Первое число наоборот:', n)
k = turn_number(k)
print('Второе число наоборот:', k)

print('Сумма:', float(n) + float(k))
