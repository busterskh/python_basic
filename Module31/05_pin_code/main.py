import itertools

numbers = [i for i in range(0, 10)]

for pin in itertools.product(numbers, repeat=4):
    print(pin)
