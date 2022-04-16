nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list.append([nice_list[i][x][v]
                  for i in range(len(nice_list))
                  for x in range(len(nice_list[i]))
                  for v in range(len(nice_list[i][x]))])
nice_list = nice_list[-1]

print(nice_list)
