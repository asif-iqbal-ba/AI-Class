#!/usr/bin/env python
# coding: utf-8

# In[1]:


mybool = True
while mybool == True:
    try:
        n = input("Enter text here or q for Quit: ")        
        if n != "q":
            nn = n[::-1]
            if nn == n:
                res = " is Palindrome"
            else:
                res = " is not a Palindrome"
            print("Text " + n + res)
        else:
            mybool = False
    except:
        print("Some Error Occured. Try Again")


# In[ ]:




