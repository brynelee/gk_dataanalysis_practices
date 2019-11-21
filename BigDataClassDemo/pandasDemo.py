import pandas as pd
import numpy as np

a = pd.Series([1,2,3,4,5])

print(a)

b = pd.Series([2,4,5,6], index=list('abcd'))

print(b)

print(b['c'])
print(b['c':'d'])
print(b[1:3])
print(b[:3])

# 使用字典创建DataFrame
df = pd.DataFrame({"name":'hello great python world'.split(), "growth":[1,5,10,23]}, index='a b c d'.split())
print(df)

# 使用numpy的ndarray来创建DataFrame
df1 = pd.DataFrame(np.random.randn(10,3), columns=["ca", "cb", "cc"], index=list("abcdefghij"))
print(df1)
print(df1.shape)

# 对数据进行统计分析
print(df1.describe())

print(df1.loc[['b','g']])

# 按行号取行
print("df1.iloc[1] is: ", df1.iloc[1])

# 取第1行和第3行
print(df1.iloc[[1,3]])
print('='*100)
# 取行1列2的数据
print(df1.iloc[1,2])
print('='*100)
# 取行1-5，列2的数据
print(df1.iloc[1:5, 2])
print('='*100)

print(df1.columns.tolist())
print('='*100)
print(pd.unique(df1['ca']))

print('='*100)
df1_after_drop = df1.drop(['ca'], axis=1)
print("df1 after drop: \n", df1_after_drop)

print('='*100)
df2 = df1
df2.iloc[1,2] = np.NaN
df2.iloc[2,1] = np.NaN
df2.iloc[3,0] = np.NaN
print("df2 by filled with NaN is: ")
print(df2)

print('='*100)
print('='*100)

# from sklearn.preprocessing import Imputer
# imp = Imputer(missing_values="NaN", strategy='mean', axis=0, copy=True)

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.NaN, strategy='mean', copy=True)

imp_mean = imp.fit(df2)
df21 = imp_mean.transform(df2)

print("df2's NaN were filled by SimpleImputer as below: ")
print(df21)
print('='*100)

from sklearn.preprocessing import LabelEncoder

df3 = np.random.randint(0, high=100, size=5)
print("df3 oringinally is: ")
print(df3)
print('='*100)

le = LabelEncoder()
le.fit(df3)
le.classes_
df4 = le.transform(df3)
print("after LabelEncoder, df3 changed to: ")
print(df4)
print('='*100)
print('='*100)

# 另外一个例子
le2 = LabelEncoder()
le2.fit([1,2,2,6])
print(le.classes_)
s1 = [1,1,2,6]
s1_encoded = le2.transform([1,1,2,6])
print("s1 after encoding is: \n", s1_encoded)
s11 = le2.inverse_transform(s1_encoded)
print("now s11 is: \n", s11)
print('='*100)




