n = int(input('Кол-во друзей: '))
k = int(input('Долговых расписок: '))

friends_list = list([0] * n)

for i in range(1, k + 1):
    print(i, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_mutch = int(input('Сколько: '))
    friends_list[to_whom - 1] -= how_mutch
    friends_list[from_whom - 1] += how_mutch

print()
for x in friends_list:
    print(friends_list.index(x) + 1, ':', x)



