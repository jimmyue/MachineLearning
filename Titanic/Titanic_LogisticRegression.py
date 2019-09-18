import pandas       #Python数据分析处理库
from sklearn.linear_model import LogisticRegression #机器学习库-逻辑回归
from sklearn import cross_validation                #机器学习库-交叉验证
import numpy as np  #Python科学计算库

titanic=pandas.read_csv('train.csv')
# print(titanic.head(3))         #获取前几行数据
# print(titanic.describe())      #获取特征的属性
# print(titanic['Age'].unique()) #获取特征的枚举值
titanic['Age']=titanic['Age'].fillna(titanic['Age'].median()) #空值用平均值代替
#初始化性别特征
titanic.loc[titanic['Sex']=='male','Sex']=0   
titanic.loc[titanic['Sex']=='female','Sex']=1
#初始化登船地点特征
titanic['Embarked']=titanic['Embarked'].fillna('S') #空值用出现频次最多代替
titanic.loc[titanic['Embarked']=='S','Embarked']=0   
titanic.loc[titanic['Embarked']=='C','Embarked']=1
titanic.loc[titanic['Embarked']=='Q','Embarked']=2
#选择分析特征
predictors=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
#初始化逻辑回归类
alg=LogisticRegression(random_state=1)
#使用逻辑回归做三次交叉验证
scores=cross_validation.cross_val_score(alg,titanic[predictors],titanic['Survived'],cv=3)
print('准确度:',scores.mean())




