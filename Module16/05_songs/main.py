violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def song_time(violator_songs, name):
    time = 0
    for i in range(len(violator_songs)):
        if violator_songs[i][0] == name:
            time += violator_songs[i][1]
            break
    return time


summ_time = 0
count_songs = int(input('\nСколько песен выбрать? '))

for i in range(1, count_songs + 1):
    print('Название', i, 'песни:', end=' ')
    name_of_song = input()
    summ_time += song_time(violator_songs, name_of_song)

print('\nОбщее время звучания песен:', round(summ_time, 2), 'минут')
