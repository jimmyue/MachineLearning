import pandas       #Python数据分析处理库
from sklearn.feature_selection import SelectKBest,f_classif #机器学习库-特征选择库
from sklearn.ensemble import RandomForestClassifier     #机器学习库-随机森林
from sklearn import cross_validation  #机器学习库-交叉验证
import matplotlib.pyplot as plt
import numpy as np  #Python科学计算库
import re

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
#初始化家庭个数特征
titanic['FamilySize']=titanic['SibSp']+titanic['Parch']
#初始化姓名个数特征
titanic['NameLength']=titanic['Name'].apply(lambda x:len(x))
#初始化姓名头衔特征
def get_title(name):#正则表达式截取头衔
	title_search=re.search(' ([A-Za-z]+)\.',name)
	if title_search:
		return title_search.group(1)
	return ""
titles=titanic['Name'].apply(get_title)
#print(pandas.value_counts(titles)) #统计枚举值的个数
title_mapping={'Mr':1,'Miss':2,'Mrs':3,'Master':4,'Dr':5,'Rev':6,'Mlle':7,'Col':8,'Major':9,'Don':10,'Countess':11,'Ms':12,'Mme':13,'Capt':14,'Lady':15,'Jonkheer':16,'Sir':17}
for k,v in title_mapping.items():
	titles[titles==k]=v
titanic['Title']=titles
predictors=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked','FamilySize','NameLength','Title']
#初始化特征选择类：通过只改变一个特征的值进行训练，与目标进行对比，从而确定是否为重要特征；
selector=SelectKBest(f_classif,k=5)
#使用函数进行训练
selector.fit(titanic[predictors],titanic['Survived'])
scores=-np.log10(selector.pvalues_)
#输出为图像，查看重要特征
plt.bar(range(len(predictors)),scores)
plt.xticks(range(len(predictors)),predictors,rotation='vertical')
plt.show()
#根据重要特征学习
predictor_new=['Pclass','Sex','Fare','Title']
alg=RandomForestClassifier(random_state=1,n_estimators=50,min_samples_split=8,min_samples_leaf=4)
#使用随机分类做三次交叉验证
kf=cross_validation.KFold(titanic.shape[0],n_folds=3,random_state=1)
scores=cross_validation.cross_val_score(alg,titanic[predictor_new],titanic['Survived'],cv=kf)
#print(dir(scores)) #查看可用属性
print('准确度:',scores.mean())