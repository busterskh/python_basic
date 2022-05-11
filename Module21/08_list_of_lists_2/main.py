nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def open_list(list):
    for i_num in list:
        if isinstance(i_num, int):
            new_list.append(i_num)
        else:
            open_list(i_num)


new_list = []
open_list(nice_list)
print(new_list)