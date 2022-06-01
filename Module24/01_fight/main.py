import random


class Warrior:

    def __init__(self):
        self.health = 100

    def unit_attack(self, attack, health):
        print('Воин {} атакует.\nУ противника осталось {} здоровья.'.format(attack, health - 20))
        return 20


warrior_1 = Warrior()
warrior_2 = Warrior()

while True:
    attack = random.randint(1, 2)
    if attack == 1:
        if warrior_2.health > 0:
            warrior_2.health -= warrior_1.unit_attack(attack, warrior_2.health)
        elif warrior_2.health <= 0:
            print(f'У противника не осталось здоровья. Воин {attack} победил.')
            break
    elif attack == 2:
        if warrior_1.health > 0:
            warrior_1.health -= warrior_2.unit_attack(attack, warrior_1.health)
        elif warrior_1.health <= 0:
            print(f'У противника не осталось здоровья. Воин {attack} победил.')
            break
