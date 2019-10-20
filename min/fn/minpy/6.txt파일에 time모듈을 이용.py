#!/usr/bin/env python
# coding: utf-8

# In[15]:


import time
a = time.time() #a에 시간값 입력
print(a) #a값 출력


# In[16]:


b = time.strftime('%m', time.localtime(time.time())) #b에 time모듈의 month를 입력
c = time.strftime('%Y', time.localtime(time.time())) #c에 time모듈의 year를 입력
print(b,c) #b, c값 출력


# In[17]:


outfile = open("6.txt", "a") #6.txt파일을 열고 내용을 추가한다.

outfile.write(c) #파일에 c의 값을 추가한다.
outfile.write(b) #파일에 b의 값을 추가한다.

outfile.close() #파일을 닫는다.


# In[18]:


infile = open("6.txt", "r") #6.txt파일을 열고 내용을 읽는다.
for line in infile:
    ilne = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word);
infile.close()


# In[ ]:




