#%%
import os
import numpy as np
import pandas as pd
# 讀取資料
app_train = pd.read_csv(r"C:\Users\Alan\Desktop\python code\cupoyML\Day4\application_train.csv")
print(app_train.shape)
print(app_train.columns)

# 前 10 row 以及前 5 個 column
app_train.iloc[:15, 1:4] 


# %%
