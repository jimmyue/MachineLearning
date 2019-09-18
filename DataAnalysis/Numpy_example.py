import numpy as np  #Numpy arrays are like souped-up Python lists
# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])
# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076
])
# Element Types
print (countries.dtype)
print (employment.dtype)
print (np.array([0, 1, 2, 3]).dtype)
print (np.array([1.0, 1.5, 2.0, 2.5]).dtype)
print (np.array([True, False, True]).dtype)
print (np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)
# Looping:
for i in range(len(countries)):
    country = countries[i]
    country_employment = employment[i]
    print ('Country {} has employment {}'.format(country,country_employment))
# Numpy Functions
print (employment.mean(),employment.std(),employment.max(),employment.sum())
# Standardize Data
standardize_values=(employment-employment.mean())/employment.std()
print(standardize_values)
# Index Arrays
is_good=employment>employment.mean()
print(countries[is_good])
# In place vs Not in place
# += is In place
a=np.array([1,2,3,4])
b=a
a+=np.array([1,1,1,1])
print(b)
# + is Not in place
a=np.array([1,2,3,4])
b=a
a=a+np.array([1,1,1,1])
print(b)
# Numpy is In place
a=np.array([1,2,3,4])
b=a
c=a[:2]
c[0]=100
print(b)
# 二维数组
# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])
#第一天客流最大的地铁站，10天的平均值
max_station=ridership[0,:].argmax()
max_station_avg=ridership[:,max_station].mean()
print(max_station_avg)
#axis=0纵向计算，axis=1横向计算
station_riders=ridership.mean(axis=0)
print(station_riders)