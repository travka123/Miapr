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

x = np.linspace(range[0], range[1], 10000)
y1 = stats.norm.pdf(x, mu1, sigma1) * pc1
y2 = stats.norm.pdf(x, mu2, sigma2) * pc2

intersection_area_start = np.argmax(y1)
intersection_area_end = np.argmax(y2)

count_for_second = not intersection_area_start < intersection_area_end
first, second = (y1, y2) if (intersection_area_start < intersection_area_end) else (y2, y1)

if count_for_second:
    intersection_area_start, intersection_area_end = intersection_area_end, intersection_area_start

intersection = intersection_area_start + np.argmin(np.abs(y1[intersection_area_start:intersection_area_end] - y2[intersection_area_start:intersection_area_end]))

false_alert = np.sum(second[:intersection]) / np.sum(second)
detection_skip = np.sum(first[intersection:]) / np.sum(first)
classification_error = false_alert + detection_skip

if count_for_second:
    false_alert, detection_skip = detection_skip, false_alert

plt.figure(figsize=(8, 8))
first_color, second_color = ("khaki", "pink") if not count_for_second else ("pink", "khaki")
plt.fill_between(x[:intersection], second[:intersection], color=first_color)
plt.fill_between(x[intersection:], first[intersection:], color=second_color)
plt.plot(x, y1)
plt.plot(x, y2)
plt.scatter(x[intersection], y1[intersection], color="black")
plt.xlabel(f"False alert (khaki): {false_alert:.{4}f} Warning skip (pink): {detection_skip:.{4}f} Classification error: {classification_error:.{4}f}")
plt.show()