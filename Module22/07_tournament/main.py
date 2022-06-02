def second_tour():
    second_tour_file = open('second_tour.txt', 'a')
    second_tour_file.write(str(next_round['players']))

    for player in range(1, next_round['players'] + 1):
        second_tour_file.write('\n' + str(player) + ') ' + ' '.join(next_round[player]))

    second_tour_file.close()
    second_tour_file = open('second_tour.txt', 'r')
    print(f'\nСодержимое файла second_tour.txt:\n{second_tour_file.read()}')
    second_tour_file.close()


def first_tour():
    first_tour_file = open('first_tour.txt', 'r')
    first_tour_result = first_tour_file.read()
    print(f'\nСодержимое файла first_tour_file.txt:\n{first_tour_result}')
    first_tour_file.close()

    first_tour_result = first_tour_result.split('\n')
    first_tour_result.sort()

    for player_number in range(1, len(first_tour_result)):
        player_stat = first_tour_result[player_number].split()
        if int(player_stat[2]) > int(first_tour_result[0]):
            next_round['players'] += 1
            next_round[next_round['players']] = player_stat[1][:1] + '.', player_stat[0], str(player_stat[2])

    second_tour()


next_round = {'players': 0}
first_tour()
