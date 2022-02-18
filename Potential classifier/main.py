import numpy as np
import matplotlib.pyplot as plt

first_class_n = int(input('first class elements number: '))
n = first_class_n + int(input('second class elements number: '))

data = np.empty((n, 2))

for i in range(n):
    print('%i element of %i class:' % ((i + 1, 1) if i < first_class_n else (i + 1 - first_class_n, 2)))
    data[i][0] = float(input('x1: '))
    data[i][1] = float(input('x2: '))

kx = np.zeros(4) # K0(x) = 0
iteration = 0
successful_sequence = 0

def apply_vec(func_vec, vec):
    func_vec[1] *= vec[0]
    func_vec[2] *= vec[1]
    func_vec[3] *= vec[0] * vec[1]
    return func_vec

def calc_vec(func_vec, vec):
    return func_vec[0] + func_vec[1] * vec[0] + func_vec[2] * vec[1] + func_vec[3] * vec[0] * vec[1]

while (successful_sequence < n) and (iteration < 1000):
    i = iteration % n
    is_first_class = i < first_class_n

    is_positive = calc_vec(kx, data[i]) > 0

    if is_positive != is_first_class:
        successful_sequence = 0

        kxx = np.array([1, 4, 4, 16]) # K(x, x) = 1 + 4x1x1i + 4x2x2i + 16x1x1ix2x2i
        p = (1 if is_first_class else -1)
        kx += p *  apply_vec(kxx, data[i])

    else:
        successful_sequence += 1

    iteration += 1

print(f'{kx[0]} {kx[1]:+}*x1 {kx[2]:+}*x2 {kx[3]:+}*x1*x2')

#start of plotting

border = 4
random_data = np.random.rand(500, 2) * border * 2 - border
ax = plt.gca()
ax.set_xlim([-border, +border])
ax.set_ylim([-border, +border])
plt.xlabel('first class - green, second class - orange')
for i in range(random_data.shape[0]):
    if calc_vec(kx, random_data[i]) > 0:
        plt.scatter(random_data[i][0], random_data[i][1], color="green")
    else:
        plt.scatter(random_data[i][0], random_data[i][1], color="orange")

if kx[3] != 0:
    x = np.arange(-border, -kx[2] / kx[3] - 0.0001, 0.01)
    y = (-kx[1] * x - kx[0]) / (kx[3] * x + kx[2])
    plt.plot(x, y, color='red')

    x = np.arange(-kx[2] / kx[3] + 0.0001, border, 0.01)
    y = (-kx[1] * x - kx[0]) / (kx[3] * x + kx[2])
    plt.plot(x, y, color='red')

else:
    x = np.arange(-border, border, 0.01)
    y = (-kx[1] * x - kx[0]) / kx[2]
    plt.plot(x, y, color='red')

plt.show()