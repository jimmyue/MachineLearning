#https://edu.hellobi.com/course/150/play/lesson/2327
import pandas as pd
from sklearn.linear_model import LogisticRegression          #机器学习库-逻辑回归
from sklearn.ensemble import RandomForestClassifier          #机器学习库-随机森林
from sklearn.cross_validation import cross_val_predict,KFold #机器学习库-交叉验证
#经典二分类，优先考虑逻辑回归，随机分离使用率高
loans=pd.read_csv('loans_clean.csv')
features=loans[loans.columns.drop('loan_status')]
target=loans['loan_status']
#(class_weight='balanced')解决训练数据loan_status比例失衡问题
penalty={0:4,1:1}
lr=LogisticRegression(class_weight=penalty)
rf=RandomForestClassifier(n_estimators=10,random_state=1)
kf=KFold(features.shape[0],random_state=1)
#修改使用算法
predictions=cross_val_predict(lr,features,target,cv=kf)
predictions=pd.Series(predictions)

#true positive   high recall
tp_filter=(predictions==1)&(loans['loan_status']==1)
tp=len(predictions[tp_filter])
#false positive  low fall-out
fp_filter=(predictions==1)&(loans['loan_status']==0)
fp=len(predictions[fp_filter])
#false negatives
fn_filter=(predictions==0)&(loans['loan_status']==1)
fn=len(predictions[fn_filter])
#true negatives
tn_filter=(predictions==0)&(loans['loan_status']==0)
tn=len(predictions[tn_filter])
#rates
tpr=tp/float((tp+fn))
fpr=fp/float((fp+tn))
print(tpr)
print(fpr)
