zen_text = open('zen.txt', 'r')
text_in_file = zen_text.read().split('\n')

for string in text_in_file[::-1]:
    print(string)

zen_text.close()
