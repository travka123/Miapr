import sys

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

if (len(sys.argv) < 2) or not sys.argv[1].isdigit():
    print('invalid parameters: python ' + sys.argv[0] + ' n')
    exit(1)

n = int(sys.argv[1])

data = np.random.rand(n, 2)
cores = np.array([0])
binding = np.zeros(n).astype(int)
deviation = np.empty(n)
cores_distance = np.empty(0)

def link_to_cores():
    for i in range(n):
        cluster_index = 0
        min_distance = 2 # > sqrt(1*1 + 1*1)
        for j in range(cores.size):
            current_distance = distance.euclidean(data[i], data[cores[j]])
            if min_distance > current_distance:
                cluster_index = j
                min_distance = current_distance
        binding[i] = cluster_index

while True:

    for i in range(n):
        deviation[i] = distance.euclidean(data[i], data[cores[binding[i]]])

    possible_core_index = np.argmax(deviation)

    if (cores_distance.size > 0) and (deviation[possible_core_index] < (np.average(cores_distance) / 2)):
        break

    cores_to_new_distances = [distance.euclidean(data[possible_core_index], data[cores[i]]) for i in range(cores.size)]
    cores_distance = np.append(cores_distance, cores_to_new_distances)
    cores = np.append(cores, [possible_core_index])

    link_to_cores()

clusters = [[] for _ in range(cores.size)]
for i in range(n):
    clusters[binding[i]].append(data[i])

for cluster in clusters:
    plt.scatter([point[0] for point in cluster], [point[1] for point in cluster])
plt.scatter([data[index][0] for index in cores], [data[index][1] for index in cores], color='black')
plt.show()

