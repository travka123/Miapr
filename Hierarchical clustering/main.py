import sys

import numpy as np
import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import dendrogram, linkage

if (len(sys.argv) < 2) or not sys.argv[1].isdigit():
    print('invalid parameters: python ' + sys.argv[0] + ' n')
    exit(1)

n = int(sys.argv[1])

data = np.zeros((n, n))

ri = 0
random_dist = np.random.rand(int((n * n - n) / 2))
for i in range(n):
    for j in range(i):
        data[i][j] = random_dist[ri]
        data[j][i] = random_dist[ri]
        ri += 1

# n = 4
# data = [[0, 5, 0.5, 2],
#         [5, 0, 1, 0.6],
#         [0.5, 1, 0, 2.5],
#         [2, 0.6, 2.5, 0]]

print (data)

def dist_linkage(matrix, reverse):
    n = len(matrix)
    vector = []

    for i in range(n):
        for j in range(i + 1, n):
            vector.append((i, j, matrix[i][j]))

    vector = sorted(vector, key=lambda dist: dist[2], reverse=reverse)

    pairs_number = n - 1

    pairs = np.empty((pairs_number, 4))

    binding = np.arange(n)

    def bind(index, value):
        if not (index < n):
            bind(int(pairs[index - n][0]), value)
            bind(int(pairs[index - n][1]), value)
        else:
            binding[index] = value

    def count(index):
        return 1 if index < binding.size else pairs[index - binding.size][3]

    i = 0
    pair_index = 0
    while pair_index < pairs_number:

        if binding[vector[i][0]] != binding[vector[i][1]]:

            child_left = binding[vector[i][0]]
            child_right = binding[vector[i][1]]
            distance = vector[i][2] if not reverse else 1 / vector[i][2]

            elem_number = count(child_left) + count(child_right)

            pairs[pair_index] = [child_left, child_right, distance, elem_number]

            bind(n + pair_index, n + pair_index)

            pair_index += 1

        i += 1

    return pairs

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title('min')
dendrogram(dist_linkage(data, False), labels=[f'x{i + 1}' for i in range(n)], ax=ax1)
ax2.set_title('max')
dendrogram(dist_linkage(data, True), labels=[f'x{i + 1}' for i in range(n)], ax=ax2)
plt.show()