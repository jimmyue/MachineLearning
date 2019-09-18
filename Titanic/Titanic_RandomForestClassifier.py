import pandas       #Python数据分析处理库
from sklearn.ensemble import RandomForestClassifier #机器学习库-随机森林
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
#初始化随机分离类：1.取样可以随机2.特征选取可以随机
#n_estimators为决策树的个数；min_samples_split为最小样本分离个数；min_samples_leaf为最小节点分离个数
alg=RandomForestClassifier(random_state=1,n_estimators=50,min_samples_split=4,min_samples_leaf=2)
#使用随机分类做三次交叉验证
kf=cross_validation.KFold(titanic.shape[0],n_folds=3,random_state=1)
scores=cross_validation.cross_val_score(alg,titanic[predictors],titanic['Survived'],cv=kf)
print('准确度:',scores.mean())