def crypto(inform):
    return [x for i, x in enumerate(inform) if is_prime(i)]


def is_prime(num):
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                return False
        return True


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
