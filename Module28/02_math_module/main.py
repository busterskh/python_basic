class MyMath:
    """
    Класс, проводящий расчеты по входящим данным.

    Функции:
        circle_len(радиус) - вычисление длины окружности
        circle_sq(радиус) - вычисление площади окружности
        cube_volume(длинна ребра) - вычисление объёма куба
        cube_volume(радиус) - вычисление площади поверхности сферы
    """

    @classmethod
    def circle_len(cls, radius) -> float:
        c = 2 * 3.14159 * radius
        return c

    @classmethod
    def circle_sq(cls, radius) -> float:
        s = 3.14159 * radius ** 2
        return s

    @classmethod
    def cube_volume(cls, long) -> float:
        v = long ** 3
        return v

    @classmethod
    def surface_area(cls, radius) -> float:
        s = 4 * 3.14159 * radius ** 2
        return s


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(long=7)
res_4 = MyMath.surface_area(radius=3)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
