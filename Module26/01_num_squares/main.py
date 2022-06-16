def square_number(n) -> list:
    for i_num in range(1,  n):
        square = i_num ** 2
        yield square


user_number = int(input('Введите число: '))
result_1 = square_number(user_number)
for num in result_1:
    print(num)


print('-' * 15)
# ---------------------------------


class SquareNum:
    def __init__(self, n) -> None:
        self.__board = n
        self.__count = 0

    def __next__(self) -> int:
        if self.__count < self.__board:
            self.__count += 1
            return self.__count ** 2
        else:
            raise StopIteration


result_2 = SquareNum(user_number)
for num in range(user_number - 1):
    print(next(result_2))


print('-' * 15)
# ----------------------------------


result_3 = [i_num ** 2 for i_num in range(1, user_number)]
for j_num in result_3:
    print(j_num)
