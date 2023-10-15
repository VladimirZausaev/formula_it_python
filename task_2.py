list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players_count = len(list_players)
first_team = list_players[0: int(players_count / 2)]
second_team = list_players[int(players_count / 2) : ]

print(first_team)
print(second_team)