class Circle:
    x = 0
    y = 0
    r = 1

    def area(self):
        s = 3.14 * self.r ** 2
        return s

    def perimeter(self):
        p = 2 * 3.14 * self.r
        return p

    def gorw_up(self, k):
        self.r *= k


def intersection():
    if (first_circle.x - first_circle.r) < (second_circle.x - second_circle.r) < (first_circle.x + first_circle.r):
        print('Круги пересекаются')
    elif (first_circle.x - first_circle.r) < (second_circle.x + second_circle.r) < (first_circle.x + first_circle.r):
        print('Круги пересекаются')
    else:
        print('Круги не пересекаются')


first_circle = Circle()
first_circle.x = 3
first_circle.y = 3
first_circle. r = 2
second_circle = Circle()
second_circle.x = 3
second_circle.y = 5
second_circle.r = 1
print(first_circle.area())
print(second_circle.perimeter())
first_circle.gorw_up(2)
print(first_circle.r)
intersection()
