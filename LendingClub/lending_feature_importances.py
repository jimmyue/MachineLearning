import pandas as pd     #Python数据分析处理库
from sklearn.feature_selection import SelectKBest,f_classif #机器学习库-特征选择库
from sklearn.ensemble import RandomForestClassifier     #机器学习库-随机森林
from sklearn import cross_validation  #机器学习库-交叉验证
import matplotlib.pyplot as plt
import numpy as np  #Python科学计算库

loans=pd.read_csv('cleaned_loans_2007_r.csv')
predictors=loans.columns.drop('loan_status')
features=loans[predictors]
target=loans['loan_status']

selector=SelectKBest(f_classif,k=5)
#使用函数进行训练
selector.fit(features,target)
scores=-np.log10(selector.pvalues_)
#输出为图像，查看重要特征
plt.bar(range(len(predictors)),scores)
plt.xticks(range(len(predictors)),predictors,rotation='vertical')
plt.show()
