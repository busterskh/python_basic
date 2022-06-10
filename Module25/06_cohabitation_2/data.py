import random


class House:
    year_money = 0
    eat_food = 0
    cat_eat = 0
    fur_coat = 0

    home_money = 100
    fridge = 50
    cat_food = 30
    dirty = 0

    def add_dirty(self):
        self.dirty += 5

    def __str__(self):
        return 'Денег в доме: {money}\n' \
               'Еды в холодильнике: {food}\n' \
               'Еды у кота: {cat_food}\n' \
               'Грязи в доме: {dirty}\n'.format(money=self.home_money,
                                                food=self.fridge,
                                                cat_food=self.cat_food,
                                                dirty=self.dirty,
                                                )


class Residents:
    residents = []
    cats = []

    def __init__(self, name):
        self.name = name
        self.satiety = 30

    def eat(self, him):
        if home.fridge >= 30:
            self.satiety += 30
            home.fridge -= 30
            print('{} ест.'.format(self.name))
            home.eat_food += 30
        elif home.fridge > 0:
            self.satiety += home.fridge
            home.fridge -= home.fridge
            print('{} ест. Еда закончилась.'.format(self.name))
            home.eat_food += home.fridge
        else:
            print('Еды нет.')
            him.one_day()

    def day(self):
        for i_resident in self.residents:
            if i_resident.satiety <= 10:
                i_resident.eat(i_resident)
            elif i_resident.satiety < 0:
                raise Exception('Симулятор закончен, {} умер от голода:('.format(i_resident.name))
            else:
                i_resident.one_day()
        for i_cat in self.cats:
            if i_cat.satiety <= 10:
                i_cat.eat(i_cat)
            elif i_cat.satiety < 0:
                raise Exception('Симулятор закончен, {} умер от голода:('.format(i_cat.name))
            else:
                i_cat.one_day()
        home.add_dirty()


class Husband(Residents):
    def __init__(self, name):
        super().__init__(name)
        self.happy = 100

    def __str__(self):
        return '{} Сытость: {} Счастье: {}'.format(self.name, self.satiety, self.happy)

    def one_day(self):
        if home.dirty > 90:
            self.happy -= 10

        if self.happy < 30:
            if self.happy < 10:
                raise Exception('Симулятор закончен, {} умер от депрессии:('.format(self.name))
            else:
                self.game()
        elif home.home_money < 1000:
            self.work()
        else:
            self.pet_the_cat()

    def game(self):
        self.happy += 20
        self.satiety -= 10
        print('{} играет в компьютерные игры.'.format(self.name))

    def work(self):
        home.home_money += 150
        self.satiety -= 10
        print('{} работает.'.format(self.name))
        home.year_money += 150

    def pet_the_cat(self):
        self.satiety -= 10
        self.happy += 5
        self.cats[random.randint(0, len(self.cats) - 1)].pat += 1
        print('{} гладит кота.'.format(self.name))


class Wife(Residents):
    def __init__(self, name):
        super().__init__(name)
        self.happy = 100

    def __str__(self):
        return '{} Сытость: {} Счастье: {}'.format(self.name, self.satiety, self.happy)

    def one_day(self):
        if home.dirty > 90:
            self.happy -= 10

        if self.happy < 30:
            if self.happy < 10:
                raise Exception('Симулятор закончен, {} умерла от депрессии:('.format(self.name))
            else:
                if home.home_money > 500:
                    self.buy_fur_coat()
                else:
                    self.pet_the_cat()
        elif home.fridge < 60:
            self.buy_food()
        elif home.cat_food < 30:
            self.buy_cat_food()
        elif home.dirty > 90:
            self.clean_house()
        else:
            if home.home_money > 1000:
                self.buy_fur_coat()
            else:
                self.pet_the_cat()

    def buy_food(self):
        count = random.randint(30, 90)
        home.fridge += count
        home.home_money -= count
        self.satiety -= 10
        print('{} покупает {} еды.'.format(self.name, count))

    def buy_cat_food(self):
        count = random.randint(30, 60)
        home.cat_food += count
        home.home_money -= count
        self.satiety -= 10
        print('{} покупает {} еды для кота.'.format(self.name, count))

    def buy_fur_coat(self):
        home.home_money -= 350
        home.fur_coat += 1
        self.happy += 60
        self.satiety -= 10
        print('{} покупает шубу.'.format(self.name))

    def clean_house(self):
        if home.dirty < 100:
            home.dirty = 0
        elif home.dirty > 100:
            home.dirty -= 100
        self.satiety -= 10
        print('{} убирает дом.'.format(self.name))

    def pet_the_cat(self):
        self.satiety -= 10
        self.happy += 5
        self.cats[random.randint(0, len(self.cats) - 1)].pat += 1
        print('{} гладит кота.'.format(self.name))


class Cat(Residents):
    def __init__(self, name):
        super().__init__(name)
        self.pat = 0

    def __str__(self):
        return '{} Сытость: {}'.format(self.name, self.satiety)

    def sleep(self):
        self.satiety -= 10
        self.pat = 0
        print('{} спит.'.format(self.name))

    def tear_wallpaper(self):
        self.satiety -= 10
        home.dirty += 5
        print('{} дерет обои.'.format(self.name))

    def eat(self, _):
        if home.cat_food >= 10:
            self.satiety += 10
            home.cat_food -= 10
            print('{} ест.'.format(self.name))
            home.cat_eat += 10
        else:
            print('Еда закончилась.')
            self.one_day()

    def one_day(self):
        if self.pat == 0:
            self.tear_wallpaper()
        else:
            self.sleep()


home = House()
husband = Husband('Jack')
wife = Wife('Mary')
cat_1 = Cat('Tom')
cat_2 = Cat('Jerry')

Residents.residents.append(husband)
Residents.residents.append(wife)
Residents.cats.append(cat_1)
Residents.cats.append(cat_2)
