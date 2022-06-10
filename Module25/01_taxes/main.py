class Property:
    tax = 0
    money = 0

    def __init__(self, worth):
        self.worth = worth

    def apartment_tax(self):
        Property.tax += self.worth / 1000
        print('Налог на квартиру: {}'.format(self.worth / 1000))

    def car_tax(self):
        Property.tax += self.worth / 200
        print('Налог на машину: {}'.format(self.worth / 200))

    def country_house_tax(self):
        Property.tax += self.worth / 500
        print('Налог на дачу: {}'.format(self.worth / 500))

    def print_info(self):
        print('Общая сумма налога: {0}'.format(self.tax))
        self.money -= self.tax
        if self.money >= 0:
            print('Останется денег после уплаты налогов: {}'.format(self.money))
        elif self.money < 0:
            print('Не хватает денег на уплату налогов: {}'.format(abs(self.money)))


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.apartment_tax()


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.car_tax()


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.country_house_tax()


property_price = input('Введите стоимость квартиры, машины и дачи через пробел: ').split()
money = int(input('Сколько у вас денег? '))
Property.money = money
apartment = Apartment(worth=int(property_price[0]))
car = Car(worth=int(property_price[1]))
country_house = CountryHouse(worth=int(property_price[2]))
country_house.print_info()




