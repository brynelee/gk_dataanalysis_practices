import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso


'''
输出结果
   如果names没有定义，则用X1 X2 X3代替
   如果Sort = True，会将系数最大的X放在最前
'''
def pretty_print_linear(coefs, names = None, sort = False):  
    if names == None:  
        names = ["X%s" % x for x in range(len(coefs))]  
    lst = zip(coefs, names)  
    if sort:  
        lst = sorted(lst,  key = lambda x:-np.abs(x[0]))  
    return " + ".join("%s * %s" % (round(coef, 3), name)  
                                   for coef, name in lst) 



for i in range(10):
    size = 10
    X_seed = np.random.normal(0,1,size)
    X1 = X_seed + np.random.normal(0, .1, size)
    X2 = X_seed + np.random.normal(0, .1, size)
    X3 = X_seed + np.random.normal(0, .1, size)
    Y = X1 + X2 + X3 + np.random.normal(0,1,size)
    X = np.array([X1, X2, X3]).T

    lr = LinearRegression()
    lr.fit(X, Y)
    print("Linear model:", pretty_print_linear(lr.coef_))

    ridge = Ridge(alpha=10)
    ridge.fit(X, Y)
    print("Ridge model:", pretty_print_linear(ridge.coef_))

    lasso = Lasso(alpha=.3)
    lasso.fit(X, Y)
    print("lasso model:", pretty_print_linear(lasso.coef_))