# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)


def count_of_num(numbers, x):
    numbers[0].extend(numbers[1])
    numbers.remove(numbers[1])
    count = numbers[0].count(x)
    return count


def remove_num(numbers, x):
    for _ in numbers[0]:
        if x in numbers[0]:
            numbers[0].remove(x)
    return numbers


numbers = [[1, 5, 3], [1, 5, 1, 5], [1, 3, 1, 5, 3, 3]]
count_five = count_of_num(numbers, 5)
numbers = remove_num(numbers, 5)
print('Кол-во цифр 5 при первом объединении:', count_five)
count_tree = count_of_num(numbers, 3)
print('Кол-во цифр 3 при первом объединении:', count_tree)
numbers.extend(numbers[0])
numbers.remove(numbers[0])
print('Итоговый список:', numbers)