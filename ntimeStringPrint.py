#!/usr/bin/env python
# coding: utf-8

# In[2]:


while True:
    mstr = input("Enter String:")
    ntime = input("How many copies of String you need:")
    try:
        print(str(ntime) + " Copies of String are " +  mstr * int(ntime))
        break
    except:
        print("Please Enter valid Copies number")


# In[ ]:




