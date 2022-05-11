def sum(list):
    result = 0
    for i_num in list:
        if isinstance(i_num, int):
            result += i_num
        else:
            result += sum(i_num)
    return result

