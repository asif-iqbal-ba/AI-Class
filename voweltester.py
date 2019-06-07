#!/usr/bin/env python
# coding: utf-8

# In[7]:


x = ["A", "E", "I", "O", "U"]
y = input("Enter a character: ")
res = ""
y = y.upper()
for z in x:    
    if y == z:
        res = "Vowel"
        break
    else:
        res = "Not Vowel"
print("Letter " + y + " is " + res)
#print(res)


# In[ ]:




