#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd #데이터 라이브러리 pandas import
df = pd.read_csv('Csvtest.csv', encoding='euc-kr') #csv읽어오기, 파일에 한글이 포함되어 있어서 인코딩 지정
df.head() #csv의 head


# In[4]:


a = df["국어"] #csv의 국어 column을 a로 지정
b = df["수학"] #csv의 수학 column을 b로 지정
c = df["영어"] #csv의 영어 column을 c로 지정

print(a) #국어 column 출력
print(b) #수학 column 출력
print(c) #영어 column 출력


# In[10]:


sum=lambda x,y,z: x+y+z; #lambda함수를 이용하여 수식 작성
print("정수의 합 : \n",sum(a,b,c)) #앞서 lambda함수로 작성한 수식을 a, b, c로적용


# In[36]:





# In[ ]:




