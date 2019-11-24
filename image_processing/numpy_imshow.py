import pylab as plt
import numpy as np

filename = r'./image_processing/example.png'

'''
img = plt.imread(filename)
plt.imshow(img) 
plt.show()
'''

import pylab as plt
from PIL import Image
import numpy as np
img = Image.open(filename)
print(img)
img_gray = img.convert('L')    #转换成灰度图像
img = np.array(img)
print(img.shape)
print(img[0])
img_gray = np.array(img_gray)
print(img_gray.shape)
print(img_gray[0])

plt.imshow(img)    # or plt.imshow(img / 255.0)，matplotlib和matlab一样，如果是float类型的图像，范围是0-1才能正常imshow，如果是uint8图像，范围则需要是0-255
plt.show()
plt.imshow(img_gray, cmap=plt.gray())    # 显示灰度图要设置cmap参数
plt.show()
plt.imshow(Image.open(filename))    # 实际上plt.imshow可以直接显示PIL格式图像
plt.show()   
