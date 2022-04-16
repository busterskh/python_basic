def is_palindrome(num_list):
    revers_list = []
    for i in range(len(num_list) - 1, -1, -1):
        revers_list.append(num_list[i])
    if num_list == revers_list:
        return True
    else:
        return False


nums = []
new_nums = []
answer = []

count_nums = int(input('Кол-во чисел: '))
for _ in range(count_nums):
    number = int(input('Число: '))
    nums.append(number)


for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        new_nums.append(nums[j])
    if is_palindrome(new_nums):
        for i_answer in range(0, i):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Последовательность:', nums)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)