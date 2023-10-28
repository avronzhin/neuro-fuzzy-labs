import math

teams = ["Зенит", "Спартак", "Локомотив"]
players = ["Кержаков", "Акинфеев", "Месси", "Роналдо"]
properties = ["Уровень игры", "Имидж", "Фан база"]
teams_count = len(teams)
players_count = len(players)
properties_count = len(properties)

teams_properties = [
    [0.65, 0.5, 0.85],
    [0.7, 0.6, 0.9],
    [0.85, 0.8, 0.6]
]

properties_players = [
    [0.35, 0.55, 0.7, 0.7],
    [0.6, 0.8, 0.9, 0.4],
    [0.3, 0.9, 0.7, 0.65]
]

max_min = list()
for i in range(0, teams_count):
    current_line = list()
    for j in range(0, players_count):
        values = list()
        for k in range(0, properties_count):
            values.append(min(teams_properties[i][k], properties_players[k][j]))
        value = max(values)
        current_line.append(value)
    max_min.append(current_line)
print(max_min)

max_prod = list()
for i in range(0, teams_count):
    current_line = list()
    for j in range(0, players_count):
        values = list()
        for k in range(0, properties_count):
            values.append(teams_properties[i][k] * properties_players[k][j])
        value = max(values)
        current_line.append(value)
    max_prod.append(current_line)
print(max_prod)

min_max = list()
for i in range(0, teams_count):
    current_line = list()
    for j in range(0, players_count):
        values = list()
        for k in range(0, properties_count):
            values.append(max(teams_properties[i][k], properties_players[k][j]))
        value = min(values)
        current_line.append(value)
    min_max.append(current_line)
print(min_max)

max_max = list()
for i in range(0, teams_count):
    current_line = list()
    for j in range(0, players_count):
        values = list()
        for k in range(0, properties_count):
            values.append(max(teams_properties[i][k], properties_players[k][j]))
        value = max(values)
        current_line.append(value)
    max_max.append(current_line)
print(max_max)

min_min = list()
for i in range(0, teams_count):
    current_line = list()
    for j in range(0, players_count):
        values = list()
        for k in range(0, properties_count):
            values.append(min(teams_properties[i][k], properties_players[k][j]))
        value = min(values)
        current_line.append(value)
    min_min.append(current_line)
print(min_min)

max_avg = list()
for i in range(0, teams_count):
    current_line = list()
    for j in range(0, players_count):
        values = list()
        for k in range(0, properties_count):
            values.append(teams_properties[i][k] + properties_players[k][j])
        value = max(values) / 2
        current_line.append(value)
    max_avg.append(current_line)
print(max_avg)

sum_prod = list()
for i in range(0, teams_count):
    current_line = list()
    for j in range(0, players_count):
        values = list()
        for k in range(0, properties_count):
            values.append(teams_properties[i][k] * properties_players[k][j])
        value =  1 / (math.exp((sum(values) * -1)) + 1)
        current_line.append(value)
    sum_prod.append(current_line)
print(sum_prod)

matrices = [max_min, max_prod, min_max, max_max, min_min, max_avg, sum_prod]


result = list()
for i in range(0, teams_count):
    line = list()
    for j in range(0, players_count):
        counter = 0

        for k in range(0, 7):
            max_list = list()
            for ii in range(0, teams_count):
                max_list.append(matrices[k][ii][j])


            if abs(matrices[k][i][j] - max(max_list)) < 0.001:
                counter = counter + 1
        line.append(counter)
    result.append(line)
print(result)