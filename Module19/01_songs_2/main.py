def total_time(count_songs):
    time = 0
    for i_songs in range(count_songs):
        print('Название {0} песни:'.format(i_songs + 1), end=' ')
        name_song = input()
        time += violator_songs[name_song]
    print('Общее время звучания песен: {0} минуты'.format(round(time, 2)))


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_songs = int(input('Сколько песен выбрать? '))
total_time(count_songs)
