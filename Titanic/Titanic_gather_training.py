import pandas       #Python数据分析处理库
from sklearn.ensemble import GradientBoostingClassifier #机器学习库-迭代决策树
from sklearn.ensemble import RandomForestClassifier     #机器学习库-随机森林
from sklearn.linear_model import LinearRegression       #机器学习库-线性回归
from sklearn.linear_model import LogisticRegression     #机器学习库-逻辑回归
from sklearn.cross_validation import KFold              #机器学习库-交叉验证
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
#配置多种机器学习算法
algorithms=[
[GradientBoostingClassifier(random_state=1,n_estimators=50,min_samples_split=8,min_samples_leaf=4),['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked','FamilySize','NameLength','Title']]
,[RandomForestClassifier(random_state=1,n_estimators=50,min_samples_split=4,min_samples_leaf=2),['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked','FamilySize','NameLength','Title']]
,[LogisticRegression(random_state=1),['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked','FamilySize','NameLength','Title']]
]
#设置交叉验证
kf=KFold(titanic.shape[0],n_folds=4,random_state=1)
#机器学习与目标比对过程
predictions=[]
for train,test in kf:
	train_target=titanic['Survived'].iloc[train]
	full_test_predictions=[]
	for alg,predictors in algorithms:
		alg.fit(titanic[predictors].iloc[train,:],train_target)
		test_predictions=alg.predict_proba(titanic[predictors].iloc[test,:].astype(float))[:,1]
		full_test_predictions.append(test_predictions)
	#可以通过修改每种算法的系数进行调整
	test_predictions=(2*full_test_predictions[0]+5*full_test_predictions[1]+2*full_test_predictions[2])/9
	test_predictions[test_predictions<=0.5]=0
	test_predictions[test_predictions>0.5]=1
	predictions.append(test_predictions)
#合并矩阵，计算准确度
predictions=np.concatenate(predictions,axis=0)
accuracy=len(predictions[predictions==titanic['Survived']])/len(predictions)
print('准确度:',accuracy)
