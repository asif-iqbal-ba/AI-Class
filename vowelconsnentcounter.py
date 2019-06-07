#!/usr/bin/env python
# coding: utf-8

# In[6]:


def counter(n):
    vowel = 0
    cons = 0
    for cha in str(n):
        cha = cha.upper()
        if cha in["A", "E", "I", "O", "U"]:
            vowel +=1
        else:
            if cha != " ":
                cons +=1
            
    return vowel, cons
mybool = True
while mybool == True:
    try:
        n = input("Enter text here or q for Quit: ")        
        if n != "q":
            #print("Reach Here")
            vowel, cons = counter(n)
            print("Result Note Spaces are not count")
            print("Vowels: " + str(vowel))
            print("Consonants: " + str(cons))
        else:
            mybool = False
    except:
        print("Error occured")


# In[ ]:





# In[ ]:




