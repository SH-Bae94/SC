#!/usr/bin/env python
# coding: utf-8

# In[10]:


import calendar

cal = calendar.month(2016,8) #calendar모듈을 이용하여 2016년 8월을 불러들인다.
print(cal) #달력을 출력한다.


# In[13]:


import os.path

outfile = open("8.txt", "w") #8.txt파일을 열고 작성한다.

if os.path.isfile("9.txt"):
    print("동일한 이름의 파일이 이미 존재합니다.")
else:
    outfile.write(cal)
outfile.close()


# In[15]:


infile = open("8.txt", "r") #8.txt파일을 열고 읽는다.
for line in infile:
    ilne = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word);
infile.close()


# In[ ]:




