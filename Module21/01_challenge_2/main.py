def num_level(n):
    if n < 1:
        return n
    else:
        num_level(n - 1)
        return print(n)


user_n = int(input('До какого числа выводим? '))

num_level(user_n)
