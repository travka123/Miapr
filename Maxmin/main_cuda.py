import math
import sys

import numpy as np
import matplotlib.pyplot as plt
from numba import *
from numba import cuda
from scipy.spatial import distance

threads_per_block = 128
blocks_per_grid = 512

if (len(sys.argv) < 2) or not sys.argv[1].isdigit():
    print('invalid parameters: python ' + sys.argv[0] + ' n')
    exit(1)

n = int(sys.argv[1])

data = np.random.rand(n, 2)
cores = np.array([0])
binding = np.zeros(n).astype(int)
deviation_device = cuda.device_array(shape=(n,), dtype=np.float32)
cores_distance = np.empty(0)

data_device = cuda.to_device(data)
binding_device = cuda.to_device(binding)
cores_device = cuda.to_device(cores)

@cuda.jit
def link_to_cores(data, cores, binding):
    start = cuda.grid(1)
    stride = cuda.gridsize(1)

    cuda.const.array_like(data)
    cuda.const.array_like(cores)

    for i in range(start, data.shape[0], stride):
        cluster_index = 0
        class_distance = 2 # > sqrt(1*1 + 1*1)
        for j in range(cores.shape[0]):
            xdif = data[i][0] - data[cores[j]][0]
            ydif = data[i][1] - data[cores[j]][1]
            current_distance = math.sqrt(xdif * xdif + ydif * ydif)
            if class_distance > current_distance:
                cluster_index = j
                class_distance = current_distance
        binding[i] = cluster_index

@cuda.jit
def count_deviation(data, cores, binding, deviation):
    start = cuda.grid(1)
    stride = cuda.gridsize(1)

    cuda.const.array_like(data)
    cuda.const.array_like(cores)
    cuda.const.array_like(binding)

    for i in range(start, data.shape[0], stride):
        xdif = data[i][0] - data[cores[binding[i]]][0]
        ydif = data[i][1] - data[cores[binding[i]]][1]
        deviation[i] = math.sqrt(xdif * xdif + ydif * ydif)

while True:

    count_deviation[blocks_per_grid, threads_per_block](data_device, cores_device, binding_device, deviation_device)
    deviation = deviation_device.copy_to_host()

    possible_core_index = np.argmax(deviation)

    if (cores_distance.size > 0) and (deviation[possible_core_index] < (np.average(cores_distance) / 2)):
        break

    cores_to_new_distances = [distance.euclidean(data[possible_core_index], data[cores[i]]) for i in range(cores.size)]
    cores_distance = np.append(cores_distance, cores_to_new_distances)
    cores = np.append(cores, [possible_core_index])
    cores_device = cuda.to_device(cores)

    link_to_cores[blocks_per_grid, threads_per_block](data_device, cores_device, binding_device)

binding = binding_device.copy_to_host()

clusters = [[[], []] for _ in range(cores.size)]
for i in range(n):
    clusters[binding[i]][0].append(data[i][0])
    clusters[binding[i]][1].append(data[i][1])

for cluster in clusters:
    plt.scatter(cluster[0], cluster[1])
plt.scatter([data[index][0] for index in cores], [data[index][1] for index in cores], color='black')
plt.show()

