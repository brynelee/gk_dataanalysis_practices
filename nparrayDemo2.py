import numpy as np

# usage is introduced by https://www.jianshu.com/p/6f58d7f39147

a = np.random.randint(2,40,size=(2,3,4))
print("a's shape is: ", a.shape)
print(a)
print("="*90)
amin_array = np.amin(a, 0)
print("a, 0 shape is: ", amin_array.shape)
print(amin_array)
print("="*90)
print(np.amin(a,1))
print("="*90)
print(np.amin(a,2))
print("="*90)
print(np.amin(a,(0,2)))