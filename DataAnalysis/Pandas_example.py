import pandas as pd  #A Pandas series is like a cross between a list and a dictionary
import numpy as np
# Life expectancy and gdp data in 2007 for 20 countries
countries_values = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]        
#Pandas the data
countries= pd.Series(countries_values)
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)
# Looping
for i in range(len(countries)):
    print ('Country {} has employment {}'.format(countries[i],life_expectancy[i]))
# Pandas functions
print (life_expectancy.max(),life_expectancy.std(),gdp.mean(),gdp.sum())
# index arrays
print (countries[gdp>=gdp.mean()])
# positively/negatively correlated    
def variable_correlation(variable1, variable2):
    both_above=(variable1>variable1.mean()) & (variable2>variable2.mean())
    both_below=(variable1<variable1.mean()) & (variable2<variable2.mean())
    is_same_direction=both_below | both_above
    num_same_direction = is_same_direction.sum()
    num_different_direction = len(variable1)-num_same_direction
    return (num_same_direction, num_different_direction)
print(variable_correlation(life_expectancy,gdp))
# Pandas Series 
employment = pd.Series(life_expectancy_values, index=countries_values)
max_country=employment.argmax()
max_value=employment.loc[max_country]
print(max_country,max_value)
# Series align
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
s=s1+s2
print(s)
print(s.dropna())
print(s1.add(s2,fill_value=0))
# Series apply
names = pd.Series(['Andre Agassi','Barry Bonds','Christopher Columbus'])
def reverse_names(names):
    reverse=names.split(' ')[1]+', '+names.split(' ')[0]
    return reverse
names = names.apply(reverse_names)
print(names.iloc[0])
# Pandas DataFrames
employment = pd.read_csv('test.csv', index_col='Country')
employment_us = employment.loc['United States']
employment_us.plot()
# Subway ridership for 5 stations on 10 different days
# 二维操作
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)
station=ridership_df.iloc[0].argmax()
print(ridership_df[station].values.mean())
#axis=index纵向计算，axis=columns横向计算
print(ridership_df.mean(axis='index'))
#pandas shift
print(ridership_df['R003'].shift(-1))
#pandas qcut
print(pd.qcut([1,0,0.8,0.6,0.2,0.9],[0, 0.6, 0.8, 1],labels=['bad', 'medium', 'good']))
#pandas 归一化
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
#列的标准化
print((grades_df-grades_df.mean())/grades_df.std())
#行的标准化
mean_diffs=grades_df.sub(grades_df.mean(axis='columns'),axis='index')
print(mean_diffs.div(grades_df.std(axis='columns'),axis='index'))

#groupby
values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
grouped_data = example_df.groupby('even')
print(grouped_data.sum()['value'])

#merge
subway_df = pd.DataFrame({
    'UNIT': ['R003', 'R003', 'R003', 'R003', 'R003', 'R004', 'R004', 'R004',
             'R004', 'R004'],
    'DATEn': ['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
              '05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ENTRIESn': [ 4388333,  4388348,  4389885,  4391507,  4393043, 14656120,
                 14656174, 14660126, 14664247, 14668301],
    'EXITSn': [ 2911002,  2911036,  2912127,  2913223,  2914284, 14451774,
               14451851, 14454734, 14457780, 14460818],
    'latitude': [ 40.689945,  40.689945,  40.689945,  40.689945,  40.689945,
                  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ],
    'longitude': [-73.872564, -73.872564, -73.872564, -73.872564, -73.872564,
                  -73.867135, -73.867135, -73.867135, -73.867135, -73.867135]
})
weather_df = pd.DataFrame({
    'DATEn': ['05-01-11', '05-01-11', '05-02-11', '05-02-11', '05-03-11',
              '05-03-11', '05-04-11', '05-04-11', '05-05-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'latitude': [ 40.689945,  40.69132 ,  40.689945,  40.69132 ,  40.689945,
                  40.69132 ,  40.689945,  40.69132 ,  40.689945,  40.69132 ],
    'longitude': [-73.872564, -73.867135, -73.872564, -73.867135, -73.872564,
                  -73.867135, -73.872564, -73.867135, -73.872564, -73.867135],
    'pressurei': [ 30.24,  30.24,  30.32,  30.32,  30.14,  30.14,  29.98,  29.98,
                   30.01,  30.01],
    'fog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'rain': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tempi': [ 52. ,  52. ,  48.9,  48.9,  54. ,  54. ,  57.2,  57.2,  48.9,  48.9],
    'wspdi': [  8.1,   8.1,   6.9,   6.9,   3.5,   3.5,  15. ,  15. ,  15. ,  15. ]
})
subway_df.merge(weather_df,on=['DATEn','hour','latitude','longitude'],how='inner')