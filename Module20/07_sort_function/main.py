def tpl_sort(input_tuple):
    new_tuple = list(input_tuple)
    for i_num in input_tuple:
        if i_num // 1 != i_num:
            return tuple(input_tuple)
    new_tuple.sort()
    return tuple(new_tuple)


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
