#!/usr/bin/env python
# coding: utf-8

# In[3]:


def numberchk(n):
    for cha in str(n):
        if cha in["0", "1"]:
            myret = True
        else:
            myret = False
            break
    return myret

def binarychang(n):
    s = 0
    while n:
        d = str(n)[0:1]  # Taking Left Most Digit
        p = len(str(n))        
        s += pow(2, p - 1) * int(d)  # Applying formula (2 Exponent X  Left most Digit
        n = str(n)[1:]  # Taking number except one digit from Right Side
        #print(s)
        #print(n)
    return s
mybool = True
while mybool == True:
    try:
        n = input("Enter a Binary Number here or q for Quit: ")        
        if n != "q":
            if numberchk(n) == False:
                n = "A" + str(n)
            print(binarychang(n))
        else:
            mybool = False
    except:
        print("Please Enter Valid Binary Number")


# In[ ]:





# In[ ]:




