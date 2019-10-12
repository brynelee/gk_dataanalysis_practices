from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt 

from sklearn.cluster import KMeans

X,y = make_blobs(n_samples=1000, n_features=2, centers=[[-1,-1],[0,0],[1,1],[2,2]], cluster_std=[0.4, 0.2,0.2,0.2])

plt.scatter(X[:,0], X[:,1], marker='o')
# plt.show()

kmodel = KMeans(n_clusters=2)

y_pred = kmodel.fit_predict(X)

plt.scatter(X[:,0], X[:, 1], c=y_pred)
# plt.show()

from sklearn import metrics
metrics.calinski_harabasz_score(X, y_pred)

kmodel1 = KMeans(n_clusters=3)
y_pred1 = kmodel1.fit_predict(X)
plt.scatter(X[:,0], X[:, 1], c=y_pred1)
# plt.show()
print(metrics.calinski_harabasz_score(X, y_pred1))

kmodel2 = KMeans(n_clusters=4)
y_pred2 = kmodel2.fit_predict(X)
print(metrics.calinski_harabasz_score(X, y_pred2))





