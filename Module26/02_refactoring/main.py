def search(x, target) -> bool:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == target:
            return True


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for x in list_1:
    if search(x, to_find):
        print('Found!!!')
        break



