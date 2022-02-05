import sys
from scipy.spatial import distance
import matplotlib.pyplot as plt
import numpy as np

if (len(sys.argv) < 3) or not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print('invalid parameters: python ' + sys.argv[0] + ' k n')
    exit(1)

k = int(sys.argv[1])
n = int(sys.argv[2])

MAX_DISTANCE = distance.euclidean([0, 0], [1, 1])

data = np.random.rand(n, 2)
cores = data[:k]

stop = False
clusters = None
while not stop:
    stop = True
    clusters = [[] for x in range(k)]

    for vector in data:
        cluster_index = 0
        class_distance = MAX_DISTANCE
        for i in range(k):
            current_distance = distance.euclidean(vector, cores[i])
            if class_distance > current_distance:
                cluster_index = i
                class_distance = current_distance
        clusters[cluster_index].append(vector)

    for i in range(k):
        current_cluster = clusters[i]
        next_cluster_core = None
        core_deviation = MAX_DISTANCE
        for current_vector in current_cluster:
            current_deviation = 0
            for vector in current_cluster:
                current_deviation += distance.euclidean(current_vector, vector)
            current_deviation /= len(current_cluster)
            if core_deviation > current_deviation:
                next_cluster_core = current_vector
                core_deviation = current_deviation
        if not np.array_equal(cores[i], next_cluster_core):
            cores[i] = next_cluster_core
            stop = False

for cluster in clusters:
    plt.scatter([point[0] for point in cluster], [point[1] for point in cluster])
plt.scatter([point[0] for point in cores], [point[1] for point in cores], color='black')
plt.show()

