from matplotlib import pyplot as plt

teams = ["Зенит", "Спартак", "Локомотив"]
print("Команды")
print(teams)

criteria = ["Состав", "Тренерский штаб", "Результативность"]
print("Критерии")
print(criteria)

print()
print()
teams_count = len(teams)
criteria_count = len(criteria)

pair_matrix = [
    [
        [1, 3, 5],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [1, 5, 2],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [1, 2, 1/3],
        [0, 0, 0],
        [0, 0, 0]]
]

for k in range(0, criteria_count):
    for i in range(0, teams_count):
        pair_matrix[k][i][0] = 1 / pair_matrix[k][0][i]
        for j in range(0, teams_count):
            pair_matrix[k][i][j] = pair_matrix[k][0][j] * pair_matrix[k][i][0]

for k in range(0, criteria_count):
    print("Матрица парных сравнений по критерию", criteria[k])
    for i in range(0, teams_count):
        print(pair_matrix[k][i])
    print()

print()

stepeni = []

for k in range(0, criteria_count):
    current_stepeni = []
    for j in range(0, teams_count):
        sum = 0
        for i in range(0, teams_count):
            sum += pair_matrix[k][i][j]
        current_stepeni.append(1 / sum)
    stepeni.append(current_stepeni)

print("Степени принадлежности при равновесных критериях")
for k in range(0, criteria_count):
    print(stepeni[k])

print()
min_values = []
for i in range(0, teams_count):
    values = []
    for k in range(0, criteria_count):
        values.append(stepeni[k][i])
    min_values.append(min(values))

print("Минимальные степени принадлежности при равновесных критериях")
print(min_values)
print()
print("Решение при равновесных критериях")
sorted_min_values = sorted(min_values, reverse=True)
for i in range(0, teams_count):
    value = sorted_min_values[i]
    index = min_values.index(value)
    print(teams[index], "-", i + 1)


criteria_pair_matrix = [
    [1, 1/3, 1/6],
    [0, 0, 0],
    [0, 0, 0]
]

print()
print()


for i in range(0, criteria_count):
    criteria_pair_matrix[i][0] = 1 / criteria_pair_matrix[0][i]
    for j in range(0, teams_count):
        criteria_pair_matrix[i][j] = criteria_pair_matrix[0][j] * criteria_pair_matrix[i][0]
print("Матрица парных сравнений критериев")
for i in range(0, criteria_count):
    print(criteria_pair_matrix[i])
print()
criteria_pair_matrix_stepeni = []
for j in range(0, teams_count):
    sum = 0
    for i in range(0, teams_count):
        sum += criteria_pair_matrix[i][j]
    criteria_pair_matrix_stepeni.append(1 / sum)

criteria_stepeni = []

for i in range(0, criteria_count):
    current_stepeni = []
    for j in range(0, teams_count):
       value = stepeni[i][j] ** criteria_pair_matrix_stepeni[i]
       current_stepeni.append(value)
    criteria_stepeni.append(current_stepeni)

print("Степени принадлежности при неравновесных критериях")
for k in range(0, criteria_count):
    print(criteria_stepeni[k])
print()


criteria_min_values = []
for i in range(0, teams_count):
    values = []
    for k in range(0, criteria_count):
        values.append(criteria_stepeni[k][i])
    criteria_min_values.append(min(values))

print("Минимальные степени принадлежности при неравновесных критериях")
print(criteria_min_values)
print()
print("Решение при неравновесных критериях")
sorted_criteria_min_values = sorted(criteria_min_values, reverse=True)
for i in range(0, teams_count):
    value = sorted_criteria_min_values[i]
    index = criteria_min_values.index(value)
    print(teams[index], "-", i + 1)

plt.figure(figsize=[8, 5])
plt.title("Равновесные критерии")
for i in range(0, teams_count):
    current_set = []
    for j in range(0, teams_count):
        current_set.append(stepeni[j][i])
    plt.plot(criteria, current_set, label=teams[i])
plt.legend()
plt.show()

plt.figure(figsize=[8, 5])
plt.title("Неравновесные критерии")
for i in range(0, teams_count):
    current_set = []
    for j in range(0, teams_count):
        current_set.append(criteria_stepeni[j][i])
    plt.plot(criteria, current_set, label=teams[i])
plt.legend()
plt.show()