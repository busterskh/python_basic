massage = input('Сообщение: ').split(' ')
new_massage = ''

for i in range(len(massage)):
    if str(massage[i]).isalpha():
        new_massage += massage[i][::-1] + ' '
    else:
        word = ''
        for x in massage[i]:
            if str(x).isalpha():
                word = x + word
            else:
                word += x
                new_massage += word
                word = ''
        new_massage += word
        new_massage += ' '

print('Новое сообщение:', new_massage)
