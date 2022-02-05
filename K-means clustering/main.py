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
centers = data[:k]

stop = False
clusters = None
while not stop:
    stop = True
    clusters = [[[], []] for x in range(k)]

    for vector in data:
        cluster_index = 0
        class_distance = MAX_DISTANCE
        for i in range(k):
            current_distance = distance.euclidean(vector, centers[i])
            if class_distance > current_distance:
                cluster_index = i
                class_distance = current_distance
        clusters[cluster_index][0].append(vector[0])
        clusters[cluster_index][1].append(vector[1])

    for i in range(k):
        next_center = np.average(clusters[i], axis=1)
        if any(centers[i] != next_center):
            centers[i] = next_center
            stop = False

for cluster in clusters:
    plt.scatter(cluster[0], cluster[1])
plt.scatter([vector[0] for vector in centers], [vector[1] for vector in centers], color='black')
plt.show()
