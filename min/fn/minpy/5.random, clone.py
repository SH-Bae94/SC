#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import copy
a = (random.randint(1,6)) #1~6의 정수를 랜덤하게 a에 입력
b = (random.randint(1,6)) #1~6의 정수를 랜덤하게 b에 입력
c = (random.random()*100) #0~100을 랜덤하게 c에 입력
print(a,b,c) # a, b, c값을 출력한다.


# In[7]:


x=[a,b,c] #x에 a, b , c값 입력
clone=copy.deepcopy(x) #copy모듈을 이용하여 x값 복사

clone[0]="A+" #복사한 내용에 0번째 내용을 "A+"로 대체
print(x) #x값 출력
print(clone) #복사하고 수정한 값을 출력


# In[ ]:




