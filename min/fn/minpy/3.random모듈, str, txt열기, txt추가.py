#!/usr/bin/env python
# coding: utf-8

# In[37]:


a = str(random.randint(1,6)) #1~6의 정수를 랜덤하게 a에 입력
b = str(random.randint(1,6)) #1~6의 정수를 랜덤하게 b에 입력
c = str(random.random()*100) #0~100을 랜덤하게 c에 입력
myList=["red", "green", "blue"] #myList에 red, green, blue입력
d = random.choice(myList) #myList에서 선택한 값을 d에 입력
print(a) #a의 값을 출력
print(b) #b의 값을 출력
print(c) #c의 값을 출력
print(d) #d의 값을 출력


# In[38]:


import os.path

outfile = open("3.txt", "a") #3.txt파일을 열고 내용을 추가한다.


outfile.write(a) #파일에 앞서 구한 a의 값을 추가
outfile.write(b) #파일에 앞서 구한 b의 값을 추가
outfile.write(c) #파일에 앞서 구한 c의 값을 추가
outfile.write(d) #파일에 앞서 구한 d의 값을 추가

outfile.close() #파일을 닫는다.


# In[39]:


infile = open("3.txt", "r") #3.txt파일을 열고 내용을 읽는다.
for line in infile:
    ilne = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word);
infile.close()


# In[ ]:




