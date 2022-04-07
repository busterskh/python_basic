def round_of_game(members_list, k, n):
    count_members = 1
    while len(members_list) > 1:
        print('\nТекущий круг людей:', members_list)
        print('Начало счёта с номера', members_list[count_members - 1])
        count_members = k % len(members_list)
        print('Выбывает человек под номером', members_list[count_members - 1])
        members_list.remove(members_list[count_members - 1])
    return members_list[0]


n = int(input('Кол-во человек: '))
members_list = list(range(1, n + 1))
k = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', k, 'человек')

winner = round_of_game(members_list, k, n)

print('\nОстался человек под номером', winner)
