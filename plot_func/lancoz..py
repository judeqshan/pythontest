import numpy as np
import math
import matplotlib.pyplot as plt
#lanczos曲线
x = np.arange(-6, 6, 0.1)
a1 = 2
a2 = 3
a3 = 5
y1 = np.sinc(x) * np.sinc(x/a1)
y2 = np.sinc(x) * np.sinc(x/a2)
y3 = np.sinc(x) * np.sinc(x/a3)
plt.plot(x,y1,label="a=2")
plt.plot(x,y2,label="a=3",linestyle="--")
plt.plot(x,y3,label="a=5",linestyle="--")
plt.title('sinc')
plt.legend()   #打上标签
plt.show()