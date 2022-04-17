correct = False
while correct is False:
    password = input('Придумайте пароль: ')
    for i_pass in password:
        if i_pass in '1234567890':
            if password != password.lower():
                correct = True
    if correct is True:
        print('Это надёжный пароль!')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
