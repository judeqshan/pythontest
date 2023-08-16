import numpy as np
import matplotlib.pyplot as plt
from numpy import polynomial as P

x = np.array([10,20,30,40,50,60,70,80])
y = np.array([174,236,305,334,349,351,342,323])

# 3 表示想要拟合的最高次项是多少。
p = P.polynomial.Polynomial.fit(x,y,deg=3)

# 表达式
# print(p)
# 343.18750000000006 + 59.98042929292918·x¹ - 96.68750000000027·x² + 15.80744949494958·x³


yvals = p(x) #拟合y值

plt.plot(x, y, 's',label='original values')
plt.plot(x, yvals, 'r',label='Power series')
plt.legend()
plt.show()