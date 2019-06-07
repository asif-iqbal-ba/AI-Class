#!/usr/bin/env python
# coding: utf-8

# In[3]:


res = ""
while True:
    no = input("Enter Number:")
    try:
        remainder = int(no) % 2
        if remainder == 0:
            res = str(no) + " is Even"
        else:
            res = str(no) + " is Odd"
        break
    except:
        print("Please Enter only number")
print(res)


# In[ ]:




