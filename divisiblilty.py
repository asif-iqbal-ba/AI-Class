#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    res = ""
    try:
        numerator = input("Please Enter numerator: ")
        denominator = input("Please Enter Denominator: ")
        rem = int(numerator) % int(denominator)
        if int(rem) == 0:
            res = "Number " + str(numerator) + " is Completly divisible by " + str(denominator)
        else:
            res = "Number " + str(numerator) + " is not Completly divisible by " + str(denominator)
        break
    except:
        print("You should only enter integer/number")
print(res) 


# In[ ]:




