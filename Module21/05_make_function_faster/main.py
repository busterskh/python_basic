factorial_dict = dict()


def calculating_math_func(data):
    if data in factorial_dict:
        result = factorial_dict[data]
    else:
        result = max(factorial_dict.values())
        for index in range(max(factorial_dict.keys()), data + 1):
            result *= index
            factorial_dict[index] = result
    result /= data ** 3
    result = result ** 10
    return result
