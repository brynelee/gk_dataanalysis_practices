#encoding=utf-8
import numpy as np
import pandas as pd
import jieba

data = pd.read_csv(r"./naive_bayes/book_remarks_data.csv")
print(data)
print('='*100)
print(data.shape)
print('='*100)
print(data.index)
print('='*100)
print("data's columns are: ", data.columns)
print('='*100)
print(data.info())
print('='*100)

col = data.iloc[:,0]
print(col)

print('='*100)

arr = col.values

for word in arr:
    print(word)

print('='*100)

#去除停用词  
stopwords = {}.fromkeys(['，', '。', '！', '这', '我', '非常'])
 
print(u"\n中文分词后结果:")

corpus = []
for a in arr:
    seglist = jieba.cut(a, cut_all=False)     #精确模式
    final = ''
    for seg in seglist:
        # seg = seg.encode('utf-8')
        if seg not in stopwords: #不是停用词的保留
            final += seg
    seg_list = jieba.cut(final, cut_all=False) 
    output = ' '.join(list(seg_list))         #空格拼接
    print(output)
    corpus.append(output)

####################################
#         第二步 计算词频
#
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
  
vectorizer = CountVectorizer() #将文本中的词语转换为词频矩阵  
X = vectorizer.fit_transform(corpus) #计算个词语出现的次数    
word = vectorizer.get_feature_names() #获取词袋中所有文本关键词  
for w in word: #查看词频结果
    print(w)
print(" ")
print(X.toarray())
 
 
####################################
#         第三步 数据分析
#
from sklearn.naive_bayes import MultinomialNB  
from sklearn.metrics import precision_recall_curve  
from sklearn.metrics import classification_report
 
#使用前8行数据集进行训练，最后两行数据集用于预测
print(u"\n\n数据分析:")

X = X.toarray()

x_train = X[:10]
print("x_train ", x_train)
x_test = X[10:]
print("x_test is ", x_test)
#1表示好评 0表示差评
y_train = [1,1,0,0,1,0,0,1,0,0]
y_test = [1,0]
 
#调用MultinomialNB分类器  
clf = MultinomialNB().fit(x_train, y_train)
pre = clf.predict(x_test)
print(u"预测结果:",pre)
print(u"真实结果:",y_test)

from sklearn.metrics import classification_report
print(classification_report(y_test, pre))

#降维绘制图形
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
newData = pca.fit_transform(X)
print(newData)
 
pre = clf.predict(X)
Y = [1,1,0,0,1,0,0,1,1,0]
import matplotlib.pyplot as plt
L1 = [n[0] for n in newData]
L2 = [n[1] for n in newData]
plt.scatter(L1,L2,c=pre,s=200)
plt.show()


