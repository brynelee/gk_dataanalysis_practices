#! /usr/bin/env python2

import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1,1]=10

print(a.shape)
print(b.shape)
print(a.dtype)
print(b)


# structured array
print("========================")
print("========================")

persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
ages = peoples[:]['age']
print(ages)
chineses = peoples[:]['chinese']
print(chineses)
maths = peoples[:]['math']
print(maths)
englishs = peoples[:]['english']
print(englishs)

print("ages average is: ", np.mean(ages))
print("chinese average is: ", np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))

print("========================")
print("========================")

x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)

print("x1 is: ", x1)
print("x2 is: ", x2)

print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))



