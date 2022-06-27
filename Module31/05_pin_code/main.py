import itertools

numbers = [i for i in range(0, 10)]

for pin in itertools.combinations_with_replacement(numbers, 4):
    print(pin)
