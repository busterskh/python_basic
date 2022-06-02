import random


def write_data(number):
    defeat = random.randint(1, 13)
    if defeat == 1:
        raise Exception
    else:
        with open('out_file.txt', 'a') as file:
            file.write(str(number) + '\n')


total_count = 0
while total_count < 777:
    user_number = int(input('Введите число: '))
    try:
        write_data(user_number)
        total_count += user_number
    except Exception:
        print('Вас постигла неудача!')
        with open('out_file.txt', 'r') as out_file:
            print('\nСодержимое файла out_file.txt: ')
            for line in out_file:
                print(line[:-1])
        break

else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
    with open('out_file.txt', 'r') as out_file:
        print('\nСодержимое файла out_file.txt: ')
        for line in out_file:
            print(line[:-1])
