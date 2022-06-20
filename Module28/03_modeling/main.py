import math


class Cube:
    """Класс, реализующий 3D куб и его площадь поверхности."""
    _side = []
    _area = 0

    @classmethod
    def area_of_cube(cls) -> None:
        for square in cls.get_side():
            cls._area += square.get_perimetr()

    @classmethod
    def set_side(cls, square) -> None:
        cls._side.append(square)

    @classmethod
    def get_area(cls) -> float:
        return cls._area

    @classmethod
    def get_side(cls) -> list:
        return cls._side


class Pyramid:
    """Класс, реализующий 3D пирамиду и ее площадь поверхности."""

    _side = []
    _area = 0

    @classmethod
    def area_of_pyramid(cls) -> None:
        for square in cls.get_side():
            cls._area += square.get_perimetr()
        cls._area += cls._side[0].base * 4

    @classmethod
    def set_side(cls, triangle) -> None:
        cls._side.append(triangle)

    @classmethod
    def get_area(cls) -> float:
        return cls._area

    @classmethod
    def get_side(cls) -> list:
        return cls._side


class Square(Cube):
    """Класс, реализующий 2D квадрат, его площадь и периметр."""
    def __init__(self, long) -> None:
        self.long = long
        self.append()

    def get_square(self) -> str:
        square = (self.long * self.long)
        return f'{square} ** 2'

    def append(self) -> None:
        Cube.set_side(square=self)

    def get_perimetr(self) -> float:
        perimetr = self.long * 4
        return perimetr


class Triangle(Pyramid):
    """Класс, реализующий 2D треугольник и его периметр."""
    def __init__(self, height, base) -> None:
        self.height = height
        self.base = base
        self.append()

    def append(self) -> None:
        Triangle.set_side(triangle=self)

    def get_perimetr(self) -> float:
        side = math.sqrt((self.base / 2) ** 2 + self.height ** 2)
        perimetr = side * 2 + self.base
        return perimetr


for _ in range(6):
    Square(long=5)

for _ in range(4):
    Triangle(base=12, height=5)

Cube.area_of_cube()
print(f'Площадь поверхности куба: {Cube.get_area()}')

Pyramid.area_of_pyramid()
print(f'Площадь поверхности пирамиды: {Pyramid.get_area()}')
