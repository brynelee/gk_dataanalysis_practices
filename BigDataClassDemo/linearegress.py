import matplotlib.pyplot as plt
import pandas as pd

x = [161,170,182,175,173,165]
y = [50,58,80,70,69,55]
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
# plt.show()

xdf = pd.DataFrame(x)
ydf = pd.DataFrame(y)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(xdf, ydf)

# x1 = 183
# y1 = model.predict(x1)
# print(y1)

plt.scatter(xdf, ydf, label='original data')
plt.plot(xdf, model.predict(xdf), label='fitting line')
# plt.show()

ypred = model.predict(xdf)
from sklearn import metrics
dia = metrics.mean_squared_error(ydf, ypred)
print(dia)

