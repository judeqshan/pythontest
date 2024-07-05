import numpy as np
from scipy import signal
x = np.arange(25).reshape(5, 5)
domain = np.identity(3)
signal.order_filter(x, domain, 0)