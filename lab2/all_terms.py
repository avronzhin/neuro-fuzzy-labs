import matplotlib.pyplot as plt
import numpy
import numpy as np

terms = ["высокий", "средний", "низкий"]
terms_len = len(terms)
# scale = ["[3.0, 3.25)", "[3.25, 3.5)", "[3.5, 3.75)", "[3.75, 4.0)",
#          "[4.00, 4.25)", "[4.25, 4.50)", "[4.50, 4.75)", "[4.75, 5.0]"]
scale = [3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75]
scale_len = len(scale)
values = [
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
            if values[k][i][j] == 0:
                values[k][i][j] = 1 / values[k][j][i]

sets = []
for k in range(0, terms_len):
    current_set = []
    for i in range(0, scale_len):
        sum = 0
        for j in range(0, scale_len):
            sum += values[k][j][i]
        current_set.append(1 / sum)
    sets.append(current_set)

hard_sets = []
mers = []
for k in range(0, terms_len):
    eigen_values, eigen_vectors = numpy.linalg.eig(np.array(values[k]))
    hard_way_fuzzy_set = eigen_vectors[:, np.argmax(eigen_values)]
    mers.append(max(eigen_values) - scale_len)
    hard_maximum = max(hard_way_fuzzy_set)
    norm_hard_way_fuzzy_set = list(map(lambda x: x / hard_maximum, hard_way_fuzzy_set))
    hard_sets.append(norm_hard_way_fuzzy_set)

plt.figure(figsize=[8, 5])
for k in range(0, terms_len):
    currents_set = sets[k]
    maximum = max(currents_set)
    norm_set = list(map(lambda x: x / maximum, currents_set))
    plt.plot(scale, norm_set, label="1.7 " + terms[k])
for k in range(0, terms_len):
    currents_set = hard_sets[k]
    maximum = max(currents_set)
    norm_set = list(map(lambda x: x / maximum, currents_set))
    plt.plot(scale, norm_set, label="1.10 " + terms[k])
print("Меры несогласованности:")
print("Высокий: ", mers[0])
print("Средний: ", mers[1])
print("Низкий: ", mers[2])
plt.legend()
plt.show()
