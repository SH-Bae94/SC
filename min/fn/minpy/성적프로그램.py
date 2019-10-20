#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd #데이터 라이브러리 pandas
df = pd.read_csv('Csvtest.csv', encoding='euc-kr') #csv읽어오기, 파일에 한글이 포함되어 있어서 인코딩 지정
df.head() #csv의 head


# In[10]:


a = df["국어"] #csv의 국어 column을 a로 지정
b = df["수학"] #csv의 수학 column을 b로 지정
c = df["영어"] #csv의 영어 column을 c로 지정

print(a) #국어 column 출력
print(b) #수학 column 출력
print(c) #영어 column 출력


# In[11]:


sum = a+b+c #국어,수학,영어 column의 합
print(sum) #column의 합 출력


# In[12]:


mean = sum/3 #국어,수학,영어 column의 평균
print(mean) #column의 평균 출력


# In[13]:


df['합계'] = sum #'합계' column에 앞서 계산한 sum을 입력
print(df) #현재의 dataframe을 출력


# In[14]:


df['평균'] = mean #'평균'column에 앞서 계산한 mean을 입력
print(df) #현재의 dataframe을 출력


# In[15]:


df['석차'] = df['합계'].rank(ascending=False) #'석차'column에 '합계'column을 통해 'ascending=False' 내림차순으로 rank 입력
print(df) #현재의 dataframe을 출력


# In[18]:


df.to_csv(r'C:\Users\BSH\min\fn\rank.csv', encoding='euc-kr') #원하는 경로에 원하는 filename으로 저장하며 한글을 위해 인코딩지정


# In[ ]:




