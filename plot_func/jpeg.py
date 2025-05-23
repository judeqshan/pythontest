import numpy as np
import math
import matplotlib.pyplot as plt
#jpeg编码的qp曲线
x = np.arange(0.1, 100, 0.1)        #从0.1到100，间隔0.1取点
y = []
for t in x:
    if t < 50:
        y_1 = 5000 / t
    else:
        y_1 = 200 - t * 2
    y.append(y_1)
plt.plot(x, y, label="qp-quality")
plt.xlabel("quality")
plt.ylabel("qp")
plt.ylim(0, 500)
plt.legend()    #显示label
plt.show()