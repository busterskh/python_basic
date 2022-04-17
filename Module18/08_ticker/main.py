first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
shift = []

for i in second_str:
    if i not in first_str:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
        break
    shift.append(second_str.index(i) - first_str.index(i))

if abs(shift[0]) == abs(shift[1]) == abs(shift[2]) == abs(shift[3]):
    print('Первая строка получается из второй со сдвигом {}.'.format(abs(shift[0])))
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
