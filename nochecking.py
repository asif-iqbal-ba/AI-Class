#!/usr/bin/env python
# coding: utf-8

# In[4]:


while True:
    res = ""
    try:
        num = input("Please Enter a number or Integer: ")
        if int(num) !=0:
            if int(num) > 0:
                res = "Positive Number Entered"
            else:
                res = "Negative Number Entered"
        else:
            res = "Zero Entered"
        break
    except:
        print("You should only enter integer/number")
print(res)

