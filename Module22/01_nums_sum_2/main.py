file_numbers = open('numbers.txt', 'r')
numbers_in_file = [int(number)
                   for string in file_numbers
                   for number in string
                   if number != ' ' and number != '\n']
sum_numbers = sum(numbers_in_file[:])
file_numbers.close()

write_answer = open('answer.txt', 'w')
write_answer.write(str(sum_numbers))
write_answer.close()
