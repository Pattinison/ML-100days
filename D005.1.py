#%%  方法一
import pandas as pd
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
        'visitor': [139, 237, 326, 456]}
visitors_1 = pd.DataFrame(data)
print(visitors_1)
visitors_1
# %%  方法二
# cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
# weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
# visitors = [139, 237, 326, 456]

# list_labels = ['city', 'weekday', 'visitor']
# list_cols = [cities, weekdays, visitors]

# zipped = list(zip(list_labels, list_cols))
# list(zip(list_labels, list_cols))
# visitors_2 = pd.DataFrame(dict(zipped))
# visitors_2
# %% 找出每個weekday的平均visitor數量
visitors_1.groupby(by="weekday")['visitor'].mean()

## 如果想找的是weekday的最大visitor數量
#visitors_1.groupby(by="weekday")['visitor'].max()

# %%  作業1
import numpy as np
data = {'國家': ['taiwan', 'japan', 'china'],
        '人口': [ np.random.randint(100, 1000), np.random.randint(1000, 10000), np.random.randint(10000, 20000)]}
data1 = pd.DataFrame(data)
data1
# %% 排序
#data1.groupby(by="國家")["人口"].max()

data1[data1['人口'] == data1['人口'].max()]['國家']
# %%
