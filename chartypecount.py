#!/usr/bin/env python
# coding: utf-8

# In[5]:


def countch(x):
    length = len(x)
    digit = 0
    letters = 0
    space = 0
    other = 0
    for i in x:
        if i.isalpha():
            letters += 1
        elif i.isnumeric():
            digit += 1
        elif i.isspace():
            space += 1        
        else:
            other += 1
    return digit, letters, space, other

mybool = True
while mybool == True:
    try:
        n = input("Enter text here or q for Quit: ")        
        if n != "q":
            no, let, sp, spe = countch(n)
            print("Numbers = " +  str(no))
            print("Alphabets = " +  str(let))
            print("Spaces = " +  str(sp))
            print("Special Characters = " +  str(spe))
        else:
            mybool = False
    except:
        print("Error Try Again")


# In[ ]:




