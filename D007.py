#%%
# 載入基本套件
import os
import pandas as pd
import numpy as np

# 讀取訓練與測試資料
data_path = r"C:\Users\Alan\Desktop\python code\cupoyML\Day7"
train_path = os.path.join(data_path, 'titanic_train.csv')
test_path = os.path.join(data_path, 'titanic_test.csv')
print(train_path)
## 讀取數據集
train = pd.read_csv(train_path)
test = pd.read_csv(test_path)
train.head()
train.shape
# %%
# 重組合併資料成為訓練 / 預測用格式
train_Y = train['Survived']
ids = test['PassengerId']
df_train = train.drop(['PassengerId', 'Survived'] , axis=1)
df_test = test.drop(['PassengerId'] , axis=1)
df = pd.concat([df_train,df_test])
df.head()
df.shape
# %%
# 秀出資料欄位的類型與數量*********
dtype_df = df.dtypes.reset_index()
#
dtype_df.columns = ["Count", "Column Type"]

dtype_df = dtype_df.groupby("Column Type").aggregate('count').reset_index()
dtype_df


# %%
#確定只有 int64, float64, object 三種類型後, 分別將欄位名稱存於三個 list 中
int_features = []
float_features = []
object_features = []
for dtype, feature in zip(df.dtypes, df.columns):
    if dtype == 'float64':
        float_features.append(feature)
    elif dtype == 'int64':
        int_features.append(feature)
    else:
        object_features.append(feature)
print(f'{len(int_features)} Integer Features : {int_features}\n')
print(f'{len(float_features)} Float Features : {float_features}\n')
print(f'{len(object_features)} Object Features : {object_features}')


# %% HW***************
df[object_features].nunique()
#df[object_features].max()
#df[object_features].mean()

# %%
df[int_features].mean()


# %%
# 請依序列出 三種特徵類型 (int / float / object) x 三種方法 (平均 mean / 最大值 Max / 相異值 nunique) 的其餘操作

## 方法一: for
type_data = {
    'Int Features': int_features,
    'Float Features': float_features,
    'Object Features': object_features}
for d in type_data:
    print(f'{d} X mean(): \n\n{df[type_data[d]].mean()}\n=================')
    print(f'{d} X max(): \n\n{df[type_data[d]].max()}\n===================')
    print(f'{d} X nunique(): \n\n{df[type_data[d]].nunique()}')

# %%
## 方法二: function
def type_process(data, group):
    print('Mean()')
    print(data[group].mean(), '\n')
    print('Max()')
    print(data[group].max(), '\n')
    print('Nunique()')
    print(data[group].nunique(), '\n')
print('=========== Int Features ==============')
print(type_process(df, int_features))    
print('=========== Float Features ============')
print(type_process(df, float_features))
print('=========== Object Features ===========')
print(type_process(df, object_features))
# %%
df[object_features].max()
# %%
