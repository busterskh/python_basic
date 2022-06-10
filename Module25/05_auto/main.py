import math
import random


class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.direction_angle = angle

    def move(self):  # Движение
        distance = int(input('\nСколько км едет автомобиль в направлении {} градусов? '.format(self.direction_angle)))
        self.x += round(math.cos(self.direction_angle * math.pi / 180) * distance, 3)
        self.y += round(math.sin(self.direction_angle * math.pi / 180) * distance, 3)

    def __str__(self):  # Информация о местонахождении
        return '\nАвтомобиль находится в точке x:{}, y:{}'.format(self.x, self.y)

    def change_direction(self, angle):  # поворот
        self.direction_angle = angle
        self.move()


class Bus(Car):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.people_count = 0
        self.money = 0

    def __str__(self):
        return '\nАвтобус находится в точке x: {0},y: {1}' \
               '\n Пассажиров в автобусе: {2}' \
               '\nДенег: {3}'.format(self.x, self.y, self.people_count, self.money)

    def entrance(self):  # Пассажиры заходят
        if 0 <= self.people_count < 21:
            self.people_count += random.randint(1, 10)
        elif 30 > self.people_count > 20:
            self.people_count += random.randint(1, (30 - self.people_count))
        else:
            print('Автобус полон, подождите следующего!')

    def exit(self):  # Пассажиры выходят
        if self.people_count > 0:
            self.people_count -= random.randint(1, self.people_count)

    def move(self):  # Движение автобуса
        self.entrance()
        print(bus)
        distance = int(input('\nСколько км едет автобус в направлении {} градусов? '.format(self.direction_angle)))
        self.x += round(math.cos(self.direction_angle * math.pi / 180) * distance, 3)
        self.y += round(math.sin(self.direction_angle * math.pi / 180) * distance, 3)
        self.money += 2 * distance * self.people_count  # стоимость за км 2 денег
        self.exit()


car = Car(0, 0, -30)
car.move()
print(car)
car.change_direction(random.randint(-180, 180))
print(car)

bus = Bus(0, 0, 20)
bus.move()
bus.change_direction(random.randint(-180, 180))
print(bus)


