#!/usr/bin/env python
# coding: utf-8

# In[16]:


a=input("실수를 입력하시오:")
b=input("실수를 입력하시오:")
c=input("실수를 입력하시오:")


# In[17]:


values=[a,b,c] #values에 a,b,c 즉 1,2,3 입력
x=max(values) #x에 values의 max값을 입력
y=min(values) #y에 values의 min값을 입력
print(x,y) #x,y값 즉 values의 max와 min값을 출력


# In[18]:


concatenate = eval('x+y') #앞서 구한 x,y를 eval을 통해 계산
print(concatenate) #계산한 값을 출력, 여기서는 3+1=4가 아닌 3과 1을 합친 31 즉 concatenate했다.


# In[20]:


d=float(a) #앞서 구한 a값을 float하여 d에 입력
e=float(b) #앞서 구한 b값을 float하여 e에 입력
f=float(c) #앞서 구한 c값을 float하여 f에 입력
sum = eval('d+e+f') #d,e,f를 eval을 통해 계산
print(sum) #계산한 값을 출력, 여기서는 1.0+2.0+3.0=6.0으로 sum이 되었다.


# In[ ]:




