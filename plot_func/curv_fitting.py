import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# 自定义函数
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 构造数据
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
rng = np.random.default_rng()
y_noise = 0.2 * rng.normal(size=xdata.size)
ydata = y + y_noise

# 拟合
popt, pcov = curve_fit(func, xdata, ydata)

## 设置参数取值范围
popt1, pcov1 = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))

# 可视化
plt.plot(xdata, ydata, 'b-', label='data')
plt.plot(xdata, func(xdata, *popt), 'r-',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.plot(xdata, func(xdata, *popt1), 'g--',
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt1))

plt.legend()
plt.show()