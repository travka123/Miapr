import numpy as np
import matplotlib.pyplot as plt

first_class_n = int(input('first class elements number: '))
n = first_class_n + int(input('second class elements number: '))

data = np.empty((n, 2))

for i in range(n):
    print('%i element of %i class:' % ((i + 1, 1) if i < first_class_n else (i + 1 - first_class_n, 2)))
    data[i][0] = float(input('x1: '))
    data[i][1] = float(input('x2: '))

def apply_vec(func_vec, vec):
    func_vec[1] *= vec[0]
    func_vec[2] *= vec[1]
    func_vec[3] *= vec[0] * vec[1]

def calc_with_vec(func_vec, vec):
    return func_vec[0] + func_vec[1] * vec[0] + func_vec[2] * vec[1] + func_vec[3] * vec[0] * vec[1]

# K0(x) = 0
kx = np.zeros(4)

p = 1
stop = False
while not stop:
    stop = True
    for i in range(n - 1):
        kxx = np.array([1, 4, 4, 16])  #K(x, x) = 1 + 4x1x1i + 4x2x2i + 16x1x1ix2x2i

        if p != 0:
            apply_vec(kxx, data[i])
            kx += p * kxx

        next_vec_class = 0 if i + 1 < first_class_n else 1
        is_positive = calc_with_vec(kx, data[i + 1]) > 0
        if is_positive == (next_vec_class == 0):
            p = 0
        else:
            stop = False
            if next_vec_class == 0:
                p = 1
            else:
                p = -1


border = 4
random_data = np.random.rand(500, 2) * border * 2 - border
ax = plt.gca()
ax.set_xlim([-border, +border])
ax.set_ylim([-border, +border])
for i in range(random_data.shape[0]):
    if calc_with_vec(kx, random_data[i]) > 0:
        plt.scatter(random_data[i][0], random_data[i][1], color="green")
    else:
        plt.scatter(random_data[i][0], random_data[i][1], color="orange")

try:
    x = np.arange(-border, -kx[2] / kx[3] - 0.01, 0.01)
    y = (-kx[1] * x - kx[0]) / (kx[3] * x + kx[2])
    plt.plot(x, y, color='red')

    x = np.arange(-kx[2] / kx[3] + 0.01, border, 0.01)
    y = (-kx[1] * x - kx[0]) / (kx[3] * x + kx[2])
    plt.plot(x, y, color='red')

finally:
    plt.show()