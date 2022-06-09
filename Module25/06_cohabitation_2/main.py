from data import *


day = 0

while day != 365:
    day += 1
    for resident in Residents.residents:
        print(resident)
    for cat in Residents.cats:
        print(cat)
    print()
    husband.day()
    print('\n{}'.format(home))
    print('День {} прошел.\n'.format(day), '–' * 30)

with open('family.txt', 'w') as history:
    history.write('Итог года:'
                  '\nДенег заработано: {money}'
                  '\nЕды съедено: {food}; '
                  '\nКошачьей еды съедено: {cat_food}'
                  '\nШуб куплено: {fur_coat}'.format(money=str(home.year_money),
                                                     food=str(home.eat_food),
                                                     cat_food=str(home.cat_eat),
                                                     fur_coat=str(home.fur_coat)
                                                     )
                  )

with open('family.txt', 'r') as history:
    year_info = history.read()
    print(year_info)
