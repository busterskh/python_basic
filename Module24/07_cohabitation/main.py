import random


class Human:
    def __init__(self, name, satiety, home):
        self.name = name
        self.satiety = satiety
        self.home = home

    def life_cicle(self):
        number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.fridge < 10:
            self.go_to_shop()
        elif self.home.bedside_table < 50:
            self.work()
        elif number == 1:
            self.work()
        elif number == 2:
            self.eat()
        else:
            self.game()

    def eat(self):
        if self.home.fridge >= 10:
            print(f'\n{self.name} поел.')
            self.home.fridge -= 10
            self.satiety += 20
        else:
            print(f'\nНе хватает продуктов в холодильнике. {self.name} идет в магазин.')
            self.go_to_shop()

    def go_to_shop(self):
        if self.home.bedside_table >= 50:
            print(f'\n{self.name} покупает продукты в магазине.')
            self.home.bedside_table -= 50
            self.home.fridge += 50
            print(f'Теперь в холодильнике {self.home.fridge} еды.')
        else:
            print(f'\nНе достаточно денег. {self.name} идет работать.')
            self.work()

    def work(self):
        print(f'\n{self.name} работает...')
        self.home.bedside_table += 50
        self.satiety -= 20
        print(f"{self.name} заработал 50 денег. Положил в тумбочку.\nВ тумбочке {self.home.bedside_table} денег.")

    def game(self):
        print(f'\n{self.name} играет...')
        self.satiety -= 20


class Home:
    fridge = 50
    bedside_table = 0


house = Home()
human_1 = Human('Ivan', 20, house)
human_2 = Human('Tom', 20, house)

day = 0
while day != 365:
    human_1.life_cicle()
    human_2.life_cicle()
    day += 1
else:
    print(f"\nГод прошел. В тумбочке {house.bedside_table} денег. В холодильнике {house.fridge} еды.")
