import random


def f(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        return x / y
    except BaseException:
        print("Что-то пошло не так с первой функцией")


def f2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        return y / x
    except BaseException:
        print("Что-то пошло не так сo второй функцией")


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))

        try:
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number], reverse=True)
            with open('result.txt', 'a') as file_2:
                for num in my_list:
                    file_2.write(str(num) + ' ')
                file_2.write('\n')

        except BaseException:
            print("Что-то пошло не так с записью")





