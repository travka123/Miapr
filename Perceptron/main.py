import numpy as np

from perceptron import Perceptron

dataset = np.array([ [ [0, 0, 1] ], [ [1, 1, 1] ], [ [-1, 1, 1] ] ])

perceptron = Perceptron(3, 3)

stop = False
iterations = 0
while not stop:
    stop = True
    iterations += 1
    for i in range(dataset.shape[0]):
        for data in dataset[i]:
            if perceptron.learn(data, i):
                stop = False

print(f"iterations: {iterations}")
print(perceptron)