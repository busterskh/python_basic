count_records = int(input('Сколько записей вносится в протокол? '))
protocol = dict()
winning_place = 1

for number_record in range(1, count_records + 1):
    user_record = input(f'{number_record} запись: ').split()
    if int(user_record[0]) > protocol.get(user_record[1], [0, 0])[0] or user_record[1] not in protocol:
        protocol[user_record[1]] = [int(user_record[0]), number_record]

print(protocol)

for key, values in sorted(protocol.items(), reverse=True):
    print(f'{winning_place}-e место.', key, values[0])
    winning_place += 1
    if winning_place > 3:
        break
