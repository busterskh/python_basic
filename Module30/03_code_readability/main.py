from typing import List


is_prime: List[int] = list(filter(lambda num:
                                  True not in [True if num % x == 0 else False for x in range(2, num)],
                                  [i for i in range(2, 1001)]
                                  )
                           )
print(is_prime)


n = 1000
a = [x for x in range(n + 1)]
a[1] = 0
is_prime_2 = []

i = 2
while i <= n:
    if a[i] != 0:
        is_prime_2.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print(is_prime_2)
