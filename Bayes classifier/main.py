import sys

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

if len(sys.argv) != 4 or not sys.argv[3].replace(".", "", 1).isdigit():
    print('invalid parameters: python ' + sys.argv[0] + ' name1.npy name2.npy P(C1)')
    exit()

data1, data2 = np.load(sys.argv[1], allow_pickle=False), np.load(sys.argv[2], allow_pickle=False)

mu1, sigma1 = np.mean(data1), np.std(data1)
mu2, sigma2 = np.mean(data2), np.std(data2)

pc1 = float(sys.argv[3])
pc2 = 1 - pc1

range = (min(np.min(data1), np.min(data2)), max(np.max(data1), np.max(data2)))

x = np.linspace(range[0], range[1], 1000)
rate1 = stats.norm.pdf(x, mu1, sigma1) * pc1
rate2 = stats.norm.pdf(x, mu2, sigma2) * pc2

rate1_max = np.argmax(rate1)
rate2_max = np.argmax(rate2)

intersection = rate1_max + np.argmin(np.abs(rate1[rate1_max:rate2_max] - rate2[rate1_max:rate2_max]))

false_alert = np.sum(rate2[:intersection]) / np.sum(rate2)
detection_skip = np.sum(rate1[intersection:]) / np.sum(rate1)
classification_error = false_alert + detection_skip

plt.figure(figsize=(8, 8))
plt.fill_between(x[:intersection], rate2[:intersection], color="khaki")
plt.fill_between(x[intersection:], rate1[intersection:], color="pink")
plt.plot(x, rate1)
plt.plot(x, rate2)
plt.scatter(x[intersection], rate1[intersection], color="black")
plt.xlabel(f"False alert: {false_alert:.{4}f} Warning skip: {detection_skip:.{4}f} Classification error: {classification_error:.{4}f}")
plt.show()