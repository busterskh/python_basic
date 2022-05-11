def shortest_sequence_range(first_arg, second_arg):
    answer = ((i_num, j_num)
              for i, i_num in enumerate(first_arg)
              for j, j_num in enumerate(second_arg)
              if i == j
              )
    return answer


string = 'abcd'
nums_tpl = (10, 20, 30, 40,)
nums_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'f'}
nums_set = {1, 2, 3, 4}
nums_list = [1, 2, 3, 4]

result = shortest_sequence_range(nums_set, string)

for x in result:
    print(x)
