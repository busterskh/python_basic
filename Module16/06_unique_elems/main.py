def create_list(count, num):
    new_list = []
    for i in range(1, count + 1):
        print('Введите', i, 'число для', num, 'списка:', end=' ')
        new_num = int(input())
        new_list.append(new_num)

    return new_list


def new_first_list(first_list, second_list):
    first_list.extend(second_list)
    for i in first_list:
        while (first_list.count(i) > 1):
            first_list.remove(i)
    return first_list


first_list = create_list(3, 'первого')
second_list = create_list(7, 'второго')
print('\nПервый список:', first_list)
print('Второй список:', second_list)

new_first_list = new_first_list(first_list, second_list)

print('\nНовый первый список с уникальными элементами:', new_first_list)