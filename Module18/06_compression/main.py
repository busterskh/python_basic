s = input('Введите строку: ')
new_s = ''
prev_sym = s[0]
count = 0

for i in s:
    if i == prev_sym:
        count += 1
    else:
        new_s += prev_sym + str(count)
        count = 1
    prev_sym = i
new_s += prev_sym + str(count)

print(new_s)