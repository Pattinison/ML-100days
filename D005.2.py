#%%
target_url = 'https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt'

import requests

try: 
    response = requests.get(target_url)
    data = response.text
except:
    print('URL not available')
else:
    print('loading data sucessfully')
    
# 用 request 傳送回來的資料不會認得斷行符號
print(len(data))
data[0:100]
# %%
# 找到換行符號，用該符號做字串分割後，把它拿掉
split_tag = '\n'
data_split = data.split(split_tag)
print(len(data_split))
data_split[0]

# ## 由於這樣分割data_split串列的最後一個會為空，所以我們要將最後一個data拿掉
data_split = data_split[:-1]

## 由於這個被切割出來的字符串，還包含了前面的序號跟後面我們需要的url，所以我們要將它切割並分裝成兩個串列
number = []
url = []
for i in range(len(data_split)):
    ## 使用符號\t來分隔
    new_list = data_split[i].split('\t')
#     print(new_list)
    # 將data分裝進對應的串列
    number.append(new_list[0])
    url.append(new_list[1])
## 這樣我們就有乾淨的url串列了
number


# %% 將txt轉換成pandas dataframe
import pandas as pd
## 創建一個Python字典將我們剛剛的number還有url數據放入
data = {
    'number': number,
    'url': url
}

df = pd.DataFrame(data)
## 只顯示前五筆
df.head(20)
# %%  讀取圖片
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt


# 請用 df.loc[...] 得到第一筆資料的連結
first_link = df.loc[0, 'url']

response = requests.get(first_link)
img = Image.open(BytesIO(response.content))

# Convert img to numpy array
img = np.array(img)
plt.imshow(img)
plt.show()



# %% 將url的list轉換成numpy array
def img2arr_fromURLs(url_list, resize = False):
    """
    請完成這個 Function
    Args
        - url_list: list of URLs
        - resize: bool
    Return
        - list of array
    """
    img_list = []
    
    for url in url_list:
        response = requests.get(url)
        print(response)
        img = Image.open(BytesIO(response.content))
        print(img)
        ## 轉成NumPy array
        img_a = np.array(img)
        img_list.append(img_a)
    
    return img_list
# %%
# 發現有Image失效了
# try: 
#     result = img2arr_fromURLs(df[0:5]['url'].values)
# except:
#     print('Image unvailable')

try: 
    result = img2arr_fromURLs(df[0:4]['url'].values)
except:
    print('Image unvailable')
else:
    print('All Image Available')
    
print("Total images that we got: %i " % len(result)) # 如果不等於 5, 代表有些連結失效囉
for im_get in result:
    plt.imshow(im_get)
    plt.show()
# %%
