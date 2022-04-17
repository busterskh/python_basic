while True:
    iP = input('Введите IP:').split('.')
    if len(iP) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
    for i in iP:
        if not i.isdigit():
            print('{} — это не целое число.'.format(i))
        elif 0 < int(i) > 255:
            print('{} превышает 255.'.format(i))
    else:
        print('IP-адрес корректен.')
        break
