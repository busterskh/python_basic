def input_data():
    total_result = 0
    with open('calc.txt', 'r') as calc:
        for line in calc:
            total_result += calculate(line)
    return total_result


def calculate(line):
    data = line.split()
    operation = '+-/*%'

    try:
        if (len(data[1]) == 1 and data[1] in operation) or data[1] == '//':
            result = eval(line)
            return result
        else:
            raise SyntaxError

    except SyntaxError:
        error_fix = input(f'Обнаружена ошибка в строке: {line} Хотите исправить?')
        if error_fix.lower() == 'да':
            new_line = input('Введите исправленную строку: ')
            return calculate(new_line)


total_sum = input_data()
print(f'\nСумма результатов: {total_sum}')
