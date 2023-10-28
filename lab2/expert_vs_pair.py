from matplotlib import pyplot as plt

terms = ["низкий", "средний", "высокий"]
terms_len = len(terms)
# scale = ["[3.0, 3.25)", "[3.25, 3.5)", "[3.5, 3.75)", "[3.75, 4.0)", "[4.00, 4.25)", "[4.25, 4.50)", "[4.50, 4.75)",
#              "[4.75, 5.0]"]
expert_count = 5
scale = [3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75]
scale_len = len(scale)
expert_values = [
    [
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1]
    ],
    [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ],
    [
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1]
    ],
    [
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1]
    ]
]

expert_fuzzy_sets = []
for i in range(0, terms_len):
    line = []
    for j in range(0, scale_len):
        value = 0
        for k in range(0, expert_count):
            value += expert_values[k][i][j]
        line.append(value / expert_count)
    expert_fuzzy_sets.append(line)

pair_values = [
    [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 0],
        [4, 3, 1, 0, 0, 0, 0, 0],
        [6, 4, 3, 1, 0, 0, 0, 0],
        [7, 5, 4, 4, 1, 0, 0, 0],
        [7, 6, 5, 5, 2, 1, 0, 0],
        [8, 7, 7, 6, 4, 2, 1, 0],
        [9, 8, 8, 7, 5, 3, 1, 1]
    ],
    [
        [1, 0, 0, 0, 0, 0, 0, 1],
        [2, 1, 0, 0, 0, 0, 1, 2],
        [3, 2, 1, 0, 0, 2, 2, 3],
        [6, 4, 2, 1, 1, 3, 5, 6],
        [6, 5, 4, 1, 1, 2, 4, 7],
        [4, 2, 2, 0, 0, 1, 2, 4],
        [2, 1, 0, 0, 0, 0, 1, 2],
        [1, 0, 0, 0, 0, 0, 0, 1]
    ],
    [
        [1, 2, 3, 5, 6, 7, 8, 9],
        [0, 1, 2, 4, 5, 7, 8, 9],
        [0, 0, 1, 1, 3, 5, 6, 8],
        [0, 0, 0, 1, 2, 4, 5, 7],
        [0, 0, 0, 0, 1, 2, 3, 5],
        [0, 0, 0, 0, 0, 1, 2, 4],
        [0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ]
]


for k in range(0, terms_len):
    for i in range(0, scale_len):
        for j in range(0, scale_len):
            if pair_values[k][i][j] == 0:
                pair_values[k][i][j] = 1 / pair_values[k][j][i]

pair_fuzzy_sets = []
for k in range(0, terms_len):
    current_set = []
    for i in range(0, scale_len):
        sum = 0
        for j in range(0, scale_len):
            sum += pair_values[k][j][i]
        current_set.append(1 / sum)
    pair_fuzzy_sets.append(current_set)

plt.figure(figsize=[8, 5])
plt.title("Black - expert method, Blue - pair method")
for k in range(0, terms_len):
    currents_set = expert_fuzzy_sets[k]
    maximum = max(currents_set)
    norm_set = list(map(lambda x: x / maximum, currents_set))
    plt.plot(scale, norm_set, color="black")
for k in range(0, terms_len):
    currents_set = pair_fuzzy_sets[k]
    maximum = max(currents_set)
    norm_set = list(map(lambda x: x / maximum, currents_set))
    plt.plot(scale, norm_set, color="blue")
plt.show()