import math


def find_coin(x, y, r):
    d = math.sqrt(x ** 2 + y ** 2)
    if r >= abs(d):
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
find_coin(x, y, r)