import random


class Karma:
    total_karma = 0
    day_count = 0

    def one_day(self):
        self.day_count += 1
        chance = random.randint(1, 10)
        if chance == 1:
            exeption = random.choice(
                    'KillError DrunkError CarCrashError GluttonyError DepressionError'.split())

            with open('karma.log', 'a', encoding='utf-8') as karma_file:
                karma_file.write('Нарушена одна из заповедей: {}\n'.format(exeption))

        else:
            self.total_karma += random.randint(1, 7)

    def print_info(self):
        print('Уровень кармы: {0} \nПрошло дней: {1}'.format(self.total_karma, self.day_count))


class Human(Karma):
    def __init__(self):
        while self.total_karma < 500:
            super().one_day()
        self.print_info()


human = Human()
