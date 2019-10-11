import numpy as np

n = np.arange(12).reshape(3,4)
print(n)
print('='*100)

m = n[0:2, 1:3]
print(m)
print('='*100)

m2 = n.reshape(2, 6)
print(m2)
print('='*100)

m3 = n*2
d = np.vstack((n, m3))
f = np.hstack((n,m3))

print(d)
print(f)
print('='*100)

