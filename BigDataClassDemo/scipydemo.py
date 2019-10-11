import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

X = np.array([8.19,2.72,6.39,8.71,4.72,2.66,3.78])
Y = np.array([7.01,2.78,6.47,6.71,4.15,4.23,4.05])

print(X)
print(Y)
print('='*100)

def err(p, x, y):
    return p[0] * x + p[1] - y

p0 = [100, 20]

ret = leastsq(err, p0, args=(X,Y))

print(ret)

plt.scatter(X,Y,color='red', label='Sample Point')

# 最小二乘的拟合参数
a, b = ret[0]

x = np.linspace(0,10,1000)
y = a * x + b

plt.plot(x, y, color='orange', label='fitting line')

plt.legend()
plt.show()


