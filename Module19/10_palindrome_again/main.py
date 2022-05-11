def check_palindrome(text):
    flag = False

    for i_word in range(len(text)):
        text = list(text[:])
        text.insert(0, text.pop())
        if text == text[::-1]:
            flag = True
            print('Можно сделать палиндромом')
            break

    if not flag:
        print('Нельзя сделать палиндромом')


text = input('ведите строку: ')
check_palindrome(text)
