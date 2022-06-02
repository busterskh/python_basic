import logging

total_count = 0
line = 0

with open('people.txt', 'r') as file:
    people = file.read().split()
    while line != len(people):
        try:
            if len(people[line]) < 3:
                raise BaseException
            else:
                total_count += len(people[line])

        except BaseException:
            print(f'Ошибка: менее трёх символов в строке {line + 1}.')
            logging.basicConfig(filename='errors.log', filemode='w', level=logging.INFO)
            logging.info(f'Ошибка: менее трёх символов в строке {str(line + 1)}.')

        line += 1

print(f'Общее количество символов: {total_count}.')

