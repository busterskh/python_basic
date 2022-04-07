def come_script(guests, name):
    if len(guests) < 6:
        print('Привет,', name + '!')
        guests.append(name)
    else:
        print('Прости,', name + ', но мест нет.')


def leave_script(guests, name):
    print('Пока,', name + '!')
    guests.remove(name)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:')
    come = input('Гость пришел или ушел? ')
    if come.casefold() == 'пришел':
        name = input('Имя гостя: ')
        come_script(guests, name)
    elif come.casefold() == 'ушел':
        name = input('Имя гостя: ')
        leave_script(guests, name)
    elif come.casefold() == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
