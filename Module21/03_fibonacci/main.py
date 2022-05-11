def fibonacci(num_pos):
    if len(fibonacci_list) < num_pos:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
        return fibonacci(num_pos)
    else:
        return fibonacci_list[-1]


fibonacci_list = [1, 1]
num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fibonacci(num_pos))