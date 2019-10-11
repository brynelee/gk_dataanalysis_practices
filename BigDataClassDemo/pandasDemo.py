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

df = pd.DataFrame({"name":'hello great python world'.split(), "growth":[1,5,10,23]}, index='a b c d'.split())
print(df)

df1 = pd.DataFrame(np.random.randn(10,3), columns=["ca", "cb", "cc"], index=list("abcdefghij"))
print(df1)
print(df1.shape)

# 对数据进行统计分析
print(df1.describe())

print(df1.loc[['b','g']])

# 按行号取行
print(df1.iloc[1])

#
print(df1.iloc[[1,3]])
print('='*100)
print(df1.iloc[1,2])
print('='*100)
print(df1.iloc[1:5, 2])
print('='*100)

print(df1.columns.tolist())
print(pd.unique(df1['ca']))

df1_after_drop = df1.drop(['ca'], axis=1)
print(df1_after_drop)

df2 = df1
df2.iloc[1,2] = np.NaN
df2.iloc[2,1] = np.NaN
df2.iloc[3,0] = np.NaN

print(df2)


from sklearn.preprocessing import Imputer

imp = Imputer(missing_values="NaN", strategy='mean', axis=0, copy=True)

df21 = imp.fit(df2)

print(df21)


imp.statistics_

imp.transform(df21)


from sklearn.preprocessing import LabelEncoder

df3 = np.random.randint(0, high=100, size=5)
print(df3)

le = labelEncoder()
le.fit(df3)
le.classes_
df4 = le.transform(df3)
print(df4)

