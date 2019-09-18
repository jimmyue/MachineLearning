import pandas as pd
#Notes offered by Prospectus (https://www.lendingclub.com/info/prospectus.action)
#读取csv文件，过滤第一行(skiprows=1)
loans_source=pd.read_csv('LoanStats3a.csv',skiprows=1)
#过滤记录超过一半为空的列(axis=1)
loans_source=loans_source.dropna(thresh=len(loans_source)/2,axis=1)
#过滤不需要的列(手工判断并选择)
loans_source=loans_source.drop(['url','desc','id','member_id','funded_amnt','funded_amnt_inv','grade','sub_grade','last_pymnt_amnt'],axis=1)
loans_source=loans_source.drop(['emp_title','issue_d','zip_code','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv'],axis=1)
loans_source=loans_source.drop(['total_rec_prncp','total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d'],axis=1)
print(loans_source.iloc[0])  #打印第一行
print(loans_source.shape)    #打印矩阵大小
#二分类，打印特征对应枚举值
print(loans_source['loan_status'].value_counts())
#过滤非二类的行
loans_source=loans_source[(loans_source['loan_status']=='Fully Paid')|(loans_source['loan_status']=='Charged Off')]
#去除只有一个枚举值的特征
orig_columns=loans_source.columns
drop_columns=[]
for col in orig_columns:
	col_series=loans_source[col].dropna().unique()
	if len(col_series)==1:
		drop_columns.append(col)
loans_source=loans_source.drop(drop_columns,axis=1)
#查看特征为null值的个数,并删除为空的列或行
print(loans_source.isnull().sum())
loans_source=loans_source.drop('pub_rec_bankruptcies',axis=1)
loans_source=loans_source.dropna(axis=0)
#查看特征数据类型
print(loans_source.dtypes.value_counts())
object_columns_df=loans_source.select_dtypes(include=['object'])
print(object_columns_df.iloc[0])
#数据清洗，转值
loans_source=loans_source.drop(['last_credit_pull_d','earliest_cr_line','addr_state','title','pymnt_plan'],axis=1)
loans_source['int_rate']=loans_source['int_rate'].str.rstrip('%').astype('float')
loans_source['revol_util']=loans_source['revol_util'].str.rstrip('%').astype('float')
Translate={'loan_status':{'Fully Paid':1,'Charged Off':0}
,'emp_length':{'10+ years':10,'9 years':9,'8 years':8,'7 years':7,'6 years':6,'5 years':5,'4 years':4,'3 years':3,'2 years':2,'1 year':1,'< 1 year':0,'n/a':9}
,'home_ownership':{'RENT':1,'MORTGAGE':2,'OWN':3,'OTHER':4,'NONE':5}
,'verification_status':{'Not Verified':1,'Verified':2,'Source Verified':3}
,'purpose':{'debt_consolidation':1,'credit_card':2,'other':3,'home_improvement':4,'major_purchase':5,'small_business':6,'car':7,'wedding':8,'medical':9,'moving':10,'vacation':11,'house':12,'educational':13,'renewable_energy':14}
,'term':{' 36 months':1,' 60 months':2}
}
loans_source=loans_source.replace(Translate)
'''
#按一个特征的多个枚举值分成多个特征,暂不知为何这样处理
cat_columns=['home_ownership','verification_status','emp_length','purpose','term']
for i in cat_columns:
	print(loans_source[i].value_counts())
dummy_df=pd.get_dummies(loans_source[cat_columns])
loans_source=pd.concat([loans_source,dummy_df],axis=1)
loans_source=loans_source.drop(cat_columns,axis=1)
'''
#清洗完数据，导出到新的CSV文件
loans_source.to_csv('loans_clean.csv',index=False)
