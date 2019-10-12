from sklearn.preprocessing import OneHotEncoder

a = [[0,0,3],[1,1,0],[0,2,1],[1,0,2]]

enc = OneHotEncoder()

enc.fit(a)

print(enc.n_values_)

print(enc.transform([[0,1,3]]).toarray())

