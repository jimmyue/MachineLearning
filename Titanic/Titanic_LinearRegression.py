import pandas       #Python数据分析处理库
from sklearn.linear_model import LinearRegression       #机器学习库-线性回归
from sklearn.cross_validation import KFold              #机器学习库-交叉验证
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
#初始化线性回归类
alg=LinearRegression()
#shape获取矩阵行列[m,n];交叉验证将m行平均分成3份做交叉验证(1,2->3;1,3->2;2,3->1)
kf=KFold(titanic.shape[0],n_folds=3,random_state=1)
predictions=[]
for train,test in kf:
	#iloc---通过行号获取训练算法的(数据、结果)行数据
	train_predictors=(titanic[predictors].iloc[train,:])
	train_target=titanic['Survived'].iloc[train]
	#使用predictors、target训练算法
	alg.fit(train_predictors,train_target)
    #使用训练的算法对test进行预测
	test_predictions=alg.predict(titanic[predictors].iloc[test,:])
	#将三次交叉测试的预测值存入predictions
	predictions.append(test_predictions)
#将三次交叉验证得到的三个矩阵合成一个矩阵
predictions=np.concatenate(predictions,axis=0)
#预测值判定，格式化输出成0,1
predictions[predictions>0.5]=1
predictions[predictions<=0.5]=0
#准确度=预测对的个数/总个数
accuracy=len(predictions[predictions==titanic['Survived']])/len(predictions)
print('准确度:',accuracy)




