import numpy
import numpy as np

values = [[1, 1 / 2, 1 / 4, 1 / 6, 1 / 8, 1 / 9], [2, 1, 1 / 3, 1 / 5, 1 / 7, 1 / 8], [4, 3, 1, 1 / 4, 1 / 4, 1 / 5],
    [6, 5, 4, 1, 1 / 3, 1 / 3], [8, 7, 4, 3, 1, 1], [9, 8, 5, 3, 1, 1]]
eigen_values, eigen_vectors = numpy.linalg.eig(np.array(values))
print("Eigen values:")
print(eigen_vectors)
hard_way_fuzzy_set = eigen_vectors[:, np.argmax(eigen_values)]
hard_maximum = max(hard_way_fuzzy_set, key=abs)
norm_hard_way_fuzzy_set = list(map(lambda x: x / hard_maximum, hard_way_fuzzy_set))
print("norm hard way fuzzy:")
print(norm_hard_way_fuzzy_set)