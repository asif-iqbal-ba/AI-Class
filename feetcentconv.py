#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    try:
        feet = input("Enter Length in Feet here: ")
        cm = float(feet) * 30.48
        print("There are " + str(cm) + " Cm in " + str(feet) +" ft")
        break
    except:
        print("Enter value in Numeric")

