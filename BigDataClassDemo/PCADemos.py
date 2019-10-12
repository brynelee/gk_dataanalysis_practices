from sklearn.decomposition import PCA
import pandas as pd

a = pd.DataFrame([[1,0.99,1.01],[2,2.01,1.99],[3.03,2.99,3]])

pca = PCA(n_components=1)
na  = pca.fit_transform(a)
print("'a' was PCAed as: na, now na is: ")
print(na)
# 保留的特征属性
print(pca.n_components_)
# 保留下来的特征属性的方差在总体特征属性的方差总体占比
print(pca.explained_variance_ratio_)


pca1 = PCA(n_components='mle')
na1 = pca1.fit_transform(a)
print("mle PCA processing is as: ")
print(na1)

pca2 = PCA(n_components=0.95)
na2 = pca2.fit_transform(a)
print("ratio target PCA result is as: ")
print(na2)
