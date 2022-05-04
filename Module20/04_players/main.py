def create_tuple():
    for i_key, i_score in players.items():
        player = [x for x in i_key]
        player.extend([j for j in i_score])

        players_list.append(tuple(player))


players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players_list = []
create_tuple()

print(players_list)
