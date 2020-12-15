import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import threading
import time

data = np.random.randn(10000)

mean = 100 #srednia
sigma = 40 #odchylenie standardowe
x = mean + sigma * data

num_bins = 20
fig, ax = plt.subplots()
n, bins, patches = ax.hist(data, num_bins, density=1, facecolor='red', alpha=0.5)

plt.xticks(bins)
plt.grid(color='white', lw=0.5, axis='x')
fig.tight_layout()
ax.set_title('Histogram')
plt.show()
