import random


class Parent:
    def __init__(self, name, age, child):
        self.name = name
        self.age = age
        self.child = child

    def print_info(self):
        kids = [name for name in self.child.keys()]
        print('Родитель:\nИмя: {}\nВозраст: {}\nДети: {}'.format(self.name, self.age, ', '.join(kids)))

    def calm_down_kid(self):
        if len(self.child.keys()) > 1:
            child_name = input('Кого хотите успокоить? (введите имя)\n').title()
            if child_name in self.child:

                if not self.child[child_name].calmness:
                    self.child[child_name].calmness = True
                    print(f'Ребенок {child_name} успокоился.')
                else:
                    print(f'Ребенок {child_name} спокоен.')

            else:
                print('В списке детей такого имени нет.')

        else:
            for name, kid in self.child.items():

                if not kid.calmness:
                    kid.calmness = True
                    print(f'{name} успокоился.')
                else:
                    print(f'{name} спокоен.')

    def feed_kid(self):
        if len(self.child.keys()) > 1:
            child_name = input('Кого хотите накормить? (введите имя)\n').title()

            if child_name in self.child:

                if self.child[child_name].hunger:
                    self.child[child_name].hunger = False
                    print(f'Ребенок {child_name} накормлен.')
                else:
                    print(f'Ребенок {child_name} не голоден.')

            else:
                print('В списке детей такого имени нет.')

        else:
            for name, kid in self.child.items():

                if kid.hunger:
                    kid.hunger = False
                    print(f'Ребенок {name} накормлен.')
                else:
                    print(f'Ребенок {name} не голоден.')


class Kid:
    def __init__(self, name, age, calmness, hunger):
        self.name = name
        self.age = age
        self.calmness = calmness
        self.hunger = hunger


def actions():
    while True:
        name = input('\nВыберете родителя (введите имя): ').title()

        if name in family.keys():
            user = int(input('\nЧто хотите сделать?\n'
                             '1. Сообщить информацию о родителе\n'
                             '2. Успокоить ребенка\n'
                             '3. Покормить ребенка\n'
                             '4. Выйти из программы\n'))
            if user == 1:
                family[name].print_info()
            elif user == 2:
                family[name].calm_down_kid()
            elif user == 3:
                family[name].feed_kid()
            elif user == 4:
                print('Программа завершена!')
                break
            else:
                print('Ошибка ввода. Вводите 1, 2, 3 или 4.')

        else:
            none_parent = input('Такого родителя нет в списке. Хотите добавить? да/нет')
            if none_parent.lower() == 'да':
                add_parents()


def children_list(parent_data):
    children = dict()
    kids = int(input(f'Сколько детей у {parent_data[0]}? '))

    for _ in range(kids):
        child_info = input('Введите через пробел имя и возраст ребенка:\n').split()

        if (int(parent_data[1]) - int(child_info[1])) > 16:
            children[child_info[0]] = Kid(child_info[0], child_info[1], random.randint(0, 1), random.randint(0, 1))
        else:
            chenge_age = input('Возраст не подходит. Хотите исправить? да/нет')

            if chenge_age.lower() == 'да':
                new_age = input(f'Введите правильный возраст для {child_info[0]}: ')

                if (int(parent_data[1]) - int(new_age)) > 16:
                    print('Теперь подходит!')
                    children[child_info[0]] = Kid(child_info[0], new_age, random.randint(0, 1), random.randint(0, 1))

    return children


def add_parents():
    parents = int(input('Сколько родителей хотите добавить? '))
    for _ in range(parents):
        parent_info = input('Введите через пробел имя и возраст родителя:\n').split()
        children = children_list(parent_info)
        parent_data = Parent(parent_info[0], parent_info[1], children)
        family[parent_info[0]] = parent_data


family = dict()

add_parents()

actions()
