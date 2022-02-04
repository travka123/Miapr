import math
import sys
from numba import *
from numba import cuda
import matplotlib.pyplot as plt
import numpy as np

@cuda.jit
def link_cores(data, cores, binding):
    start = cuda.grid(1)
    stride = cuda.gridsize(1)

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
def count_deviation(data, binding, deviation):
    start = cuda.grid(1)
    stride = cuda.gridsize(1)

    for i in range(start, data.shape[0], stride):
        cluster_index = binding[i]
        current_deviation = 0
        for j in range(binding.size):
            if binding[j] == cluster_index:
                xdif = data[j][0] - data[i][0]
                ydif = data[j][1] - data[i][1]
                current_deviation += math.sqrt(xdif * xdif + ydif * ydif)
        deviation[i] = current_deviation

def set_cores(cores, binding, deviation):
    changed = False
    for i in range(deviation.size):
        if (deviation[i] < deviation[cores[binding[i]]]):
            cores[binding[i]] = i
            changed = True
    return changed

if (len(sys.argv) < 3) or not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print('invalid parameters: python ' + sys.argv[0] + ' k n')
    exit(1)

k = int(sys.argv[1])
n = int(sys.argv[2])

data = np.random.rand(n, 2)
cores = np.arange(k)

data_device = cuda.to_device(data)

threads_per_block = 128
blocks_per_grid = 272

binding = None
stop = False
while not stop:
    binding_device = cuda.device_array(shape=(n,), dtype=int)
    cores_device = cuda.to_device(cores)

    link_cores[blocks_per_grid, threads_per_block](data_device, cores_device, binding_device)

    deviation_device = cuda.device_array(shape=(n,), dtype=np.float32)

    count_deviation[blocks_per_grid, threads_per_block](data_device, binding_device, deviation_device)

    binding = binding_device.copy_to_host()
    deviation = deviation_device.copy_to_host()
    stop = not set_cores(cores, binding, deviation)

clusters = [[] for _ in range(k)]
for i in range(n):
    clusters[binding[i]].append(data[i])

for cluster in clusters:
    plt.scatter([point[0] for point in cluster], [point[1] for point in cluster])
plt.scatter([data[index][0] for index in cores], [data[index][1] for index in cores], color='black')
plt.show()