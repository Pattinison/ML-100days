#%%
# 載入基本套件
import os
import pandas as pd
import numpy as np

# 讀取訓練與測試資料
app_train = pd.read_csv(r"C:\Users\Alan\Desktop\python code\cupoyML\Day7\application_train.csv") 
app_train.head()
# %%
## 導入視覺化套件
import matplotlib.pyplot as plt

## 更進一步了解數據集 - 統計
app_train.describe()

# %%  將三種不同類型的特徵分類 
# int_features, float_features, object_features
int_features = []
float_features = []
object_features = []
for dtype, feature in zip(app_train.dtypes, app_train.columns):
    if dtype == 'int64':
        int_features.append(feature)
    elif dtype == 'float64':
        float_features.append(feature)
    else:
        object_features.append(feature) 

# %% 計算三種不同類型的特徵的平均數、標準差
app_train[int_features].describe()
#app_train[int_features].mean()
#app_train[int_features].std()
# %%
app_train[float_features].describe()
# app_train[float_features].mean()
# app_train[float_features].std()
# %%
app_train[object_features].describe()
# app_train[object_features].mean()
# app_train[object_features].std()


# %%
#拿其中一個欄位來計算平均數、標準差 ex. AMT_INCOME_TOTAL
## https://chrisalbon.com/code/python/data_wrangling/pandas_dataframe_descriptive_stats/
print('計算AMT_INCOME_TOTAL平均數: ', app_train['AMT_INCOME_TOTAL'].mean())
# app_train['AMT_INCOME_TOTAL'].max()
# app_train['AMT_INCOME_TOTAL'].min()
print('計算AMT_INCOME_TOTAL標準差: ', app_train['AMT_INCOME_TOTAL'].std())


# %% 畫直方圖、長條圖 ex. OWN_CAR_AGE

## 方法一 pandas
app_train['OWN_CAR_AGE'].plot.hist(alpha = 0.8);


# %% plt
## 方法二
plt.hist(app_train['OWN_CAR_AGE'], color = 'g')
plt.title('OWN_CAR_AGE')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
# %%
plt.hist(app_train["TARGET"]);
# 要省略中間的話
plt.bar(["0","1"],app_train["TARGET"].value_counts());

# %%
