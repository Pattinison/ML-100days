#%%
import os
import numpy as np
import pandas as pd
## 設定數據集路徑
data_path = r"C:\Users\Alan\Desktop\python code\cupoyML\Day6\data"
train_path = os.path.join(data_path, 'application_train.csv')
test_path = os.path.join(data_path, 'application_test.csv')
print(train_path)
print(test_path)
## 讀取數據集
app_train = pd.read_csv(train_path)
app_test = pd.read_csv(test_path)
app_train.head()
# %%
## 把所有特徵的數據類型列出來
print(app_train.dtypes)
print(app_test.dtypes)
app_train.dtypes.value_counts()
#app_test.dtypes.value_counts()
# %%
## pd.Series.nunique: 用來獲取唯一值的統計次數
## select_dtypes: 用來指定特定數據類型的特徵欄位
app_train.select_dtypes(include = ["int64", "float64"])

# %%
## 檢視符合int64資料類型的特徵欄位中各自類別的數量
app_train.select_dtypes(include = ["int64"]).apply(pd.Series.nunique, axis = 0)
#app_train.select_dtypes(include = ["float64"]).apply(pd.Series.nunique, axis = 0)
#app_train.select_dtypes(include=["object"]).apply(pd.Series.nunique, axis = 0)


# %%
from sklearn.preprocessing import LabelEncoder
## 將所有為object資料類型，且其中的類別數量小於2的特徵進行Label Encoding

## 創建Label Encoder物件
le = LabelEncoder()
## 用來紀錄執行Label Encoding的次數
le_count = 0

## 開始遍歷各個特徵欄位
for col in app_train:
    ## 檢查當此特徵欄位為object資料類型(字符串)
    if app_train[col].dtype == 'object':
        ## 檢查當此欄位的類別數量小於2，就執行Label Encoding轉換
        if len(list(app_train[col].unique())) <= 2:
            ## 擬和
            le.fit(app_train[col])
            ## 轉換
            app_train[col] = le.transform(app_train[col])
            app_test[col] = le.transform(app_test[col])
    
            ## 紀錄執行label Encoding的次數加1
            le_count += 1
        
print('%d columns were label encoded.'%le_count)


# %% one hot
app_train = pd.get_dummies(app_train)
app_test = pd.get_dummies(app_test)

print(app_train['CODE_GENDER_F'].head())
print(app_train['CODE_GENDER_M'].head())
print(app_train['NAME_EDUCATION_TYPE_Academic degree'].head())

app_train
# %% HomeWork============================================

import os
import numpy as np
import pandas as pd

# 設定 data_path, 並讀取 app_train
data = r"C:\Users\Alan\Desktop\python code\cupoyML\Day6\data"
train = os.path.join(data, 'application_train.csv')
app_train = pd.read_csv(train)

sub_train = pd.DataFrame(app_train['WEEKDAY_APPR_PROCESS_START'])
print(sub_train.shape)
sub_train.head()

# %% onehot encoding
sub_train = pd.get_dummies(sub_train)
print(sub_train.shape)
sub_train.head()