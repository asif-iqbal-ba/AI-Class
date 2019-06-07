#!/usr/bin/env python
# coding: utf-8

# In[6]:


while True:
    try:
        n = input("Enter value of n here: ")
        sum_n = int((int(n) * (int(n) + 1)) / (2))
        print("Sum of n Positive integers till " + str(n) + " is " + str(sum_n))
        break
    except:
        print("Enter value in Numeric")        


# In[ ]:




