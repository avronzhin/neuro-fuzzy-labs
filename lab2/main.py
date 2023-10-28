import matplotlib.pyplot as plt


# scale = ["[3.0, 3.25)", "[3.25, 3.5)", "[3.5, 3.75)", "[3.75, 4.0)",
#          "[4.00, 4.25)", "[4.25, 4.50)", "[4.50, 4.75)", "[4.75, 5.0]"]
scale = [3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75]
values = [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [2, 1, 0, 0, 0, 0, 0, 0],
            [4, 3, 1, 0, 0, 0, 0, 0],
            [6, 4, 3, 1, 0, 0, 0, 0],
            [7, 5, 4, 4, 1, 0, 0, 0],
            [7, 6, 5, 5, 2, 1, 0, 0],
            [8, 7, 7, 6, 4, 2, 1, 0],
            [9, 8, 8, 7, 5, 3, 1, 1]
        ]

scale_len = len(scale)

for i in range(0, scale_len):
    for j in range(0, scale_len):
        if values[i][j] == 0:
            values[i][j] = 1 / values[j][i]

upper_set = []
for i in range(0, scale_len):
    sum = 0
    for j in range(0, scale_len):
        sum += values[j][i]
    upper_set.append(1 / sum)

plt.figure(figsize=[8, 5])
plt.plot(scale, upper_set)
maximum = max(upper_set)
norm = list(map(lambda x: x / maximum, upper_set))
plt.plot(scale, norm)
plt.show()