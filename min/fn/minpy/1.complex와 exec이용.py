#!/usr/bin/env python
# coding: utf-8

# In[8]:


statements = '''
import math
def area_of_circle(r):
    area_of_circle = r * r * math.pi
    return area_of_circle
'''


# In[9]:


exec(statements)


# In[12]:


a = area_of_circle(5)
b = area_of_circle(5)
c = complex(a,b)
print(c)


# In[ ]:




