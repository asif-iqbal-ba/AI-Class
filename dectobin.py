#!/usr/bin/env python
# coding: utf-8

# In[15]:


def myfun(n):
    quotient = n / 2
    remainder = n % 2
    return quotient,remainder

i = 0
j = 0
mybool = True
while mybool == True:
    try:
        # i +=1
        # print("i")
        # print(i)
        n = input("Enter Number here or q for Quit: ")
        if n != "q":
            myr = ""
            while n:
                # j +=1
                # print("j")
                # print(j)
                q, r = myfun(int(n))
                n = int(q)
                myr = str(myr) + str(r)
                #print(n)
                #print(myr)
            print(myr[::-1])
        else:
            mybool = False
    except:
        print("Enter Valid Number")
        


# In[ ]:




