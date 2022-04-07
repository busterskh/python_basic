def list_roller_skates(count):
    for i in range(1, count + 1):
        print('Размер', i, 'пары:', end=' ')
        size = int(input())
        size_roller_skates.append(size)


def list_foot_size(count):
    for i in range(1, count + 1):
        print('Размер ноги', i, 'человека:', end=' ')
        size = int(input())
        foot_size.append(size)


def comparison_list():
    count = 1
    for i in size_roller_skates[::-count]:
        for x in foot_size[::-count]:
            if x == i:
                count += 1
                break
            elif i > x:
                count += 1
                break
    return count


size_roller_skates = []
foot_size = []

count_roller = int(input('Кол-во коньков: '))
list_roller_skates(count_roller)
count_foot = int(input('\nКол-во людей: '))
list_foot_size(count_foot)

count_happy_people = comparison_list()

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_happy_people)