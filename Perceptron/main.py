import numpy as np

dataset = np.array([ [ [0, 0, 1] ], [ [1, 1, 1] ], [ [-1, 1, 1] ] ])

c = 1
w = np.zeros((3, 3))

iterations = 0
stop = False
while not stop:
    iterations += 1
    stop = True
    for i in range(dataset.shape[0]):
        for data in dataset[i]:

            rwv = np.dot(data, w[i])
            hwi = []

            for j in range(i):
                d = np.dot(data, w[j])
                if d >= rwv:
                    hwi.append(j)

            for j in range(i + 1, w.shape[0]):
                d = np.dot(data, w[j])
                if d >= rwv:
                    hwi.append(j)

            if len(hwi) > 0:
                stop = False
                wc = c * data
                w[i] += wc
                for j in range(len(hwi)):
                    w[hwi[j]] -= wc

print(f"iterations: {iterations}")
for i in range(w.shape[0]):
    func_str = f"d{i}(x) = "
    for j in range(w.shape[1]):
        func_str += f"{w[i][j]:+} * x{j + 1} "
    print(func_str)




