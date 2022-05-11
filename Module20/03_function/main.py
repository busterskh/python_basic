def slicer(random_number, element):
    index_elements = []
    if element in random_number:
        for i, x in enumerate(random_number):
            if x == element:
                index_elements.append(i)

    if len(index_elements) > 1:
        new_tuple = random_number[index_elements[0]: index_elements[1] + 1]
    elif len(index_elements) == 1:
        new_tuple = random_number[index_elements[0]:]
    else:
        new_tuple = ()

    return new_tuple


# element = int(input())
# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), element))