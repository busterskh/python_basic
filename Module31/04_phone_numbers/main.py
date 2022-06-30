import re


def check_num():
    for i_num in numbers_list:
        print(f'{numbers_list.index(i_num) + 1} номер:', end=' ')
        check_number = re.match(number_pattern, i_num)
        if check_number is not None:
            print('всё в порядке')
        else:
            print('не подходит')


numbers_list = ['9999999999', '999999-999', '99999x9999', '888888888', '7898995463']

number_pattern = r'[89]\d{9}'
check_num()
