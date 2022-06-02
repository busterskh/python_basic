class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:

    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatos:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatos]):
            print('Картошка еще не созрела!\n')
            return True
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return False


class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def take_care_of_the_garden(self):
        if self.garden.are_all_ripe():
            self.garden.grow_all()

    def harvest(self):
        storage.append(len(self.garden.potatos))
        print('Садовник собрал урожай.')
        print(f"В хранилище сейчас {sum(storage)} шт картошки")

    def new_harvest(self):
        print('Сажаем новую грядку...')
        self.garden = PotatoGarden(5)
        for index in self.garden.potatos:
            index.print_state()


storage = []
fun_farm = Gardener('Ivan', PotatoGarden(5))
while True:
    what_we_do = input('\n1. Ухаживать за грядкой.\n'
                       '2. Собирать с неё урожай.\n'
                       '3. Посадить новый урожай.\n'
                       'Что делаем?\n')
    if what_we_do == '1':
        fun_farm.take_care_of_the_garden()
    elif what_we_do == '2':
        fun_farm.harvest()
    elif what_we_do == '3':
        fun_farm.new_harvest()



