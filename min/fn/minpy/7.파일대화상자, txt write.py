#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if( readFile != None):
    infile = open(readFile, "r") #tkinter를 통해 파일대화상자로 파일을 읽어들인다.
    
for line in infile.readlines():
    line = line.strip()
    print(line)
    
infile.close()


# In[2]:


import os.path

outfile = open("7.txt", "w") #7.txt파일을 열고 작성한다.

outfile.write(line) #파일에 line을 입력한다.
    
outfile.close() #파일을 닫는다.                  


# In[3]:


infile = open("7.txt", "r") #7.txt파일을 열고 읽는다.
for line in infile:
    ilne = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word);
infile.close()


# In[ ]:




