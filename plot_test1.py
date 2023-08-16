import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = np.exp(x)

plt.plot(x, y)
plt.show()