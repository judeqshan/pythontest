#!/etc/bin/python
#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((10, 2))
y = [(0, -82.5), (1, -60.0), (2, -56.0), (3, -52.0), (4, -48.4), (5, -44.4), (6, -41.4), (7, -39.4), (8, -37.4), (9, -35.4), (10, -33.3), (20, -19.4), (25, -16.0), (30, -14.8), (40, -12.4), (50, -10.0), (60, -8.4), (70, -6.8), (75, -6.0), (80, -5.4), (90, -4.2), (100, -3.0)]
print(y)
plt.figure(figsize=(7,5))
plt.plot(y, lw = 3)
plt.plot(y, 'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A simple plot')
plt.show()
