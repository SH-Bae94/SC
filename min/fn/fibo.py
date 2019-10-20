#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fib(n):
    a,b = 0,1
    while b < n:
        print(b, end='')
        a,b = b, a+b
    print()


# In[ ]:




