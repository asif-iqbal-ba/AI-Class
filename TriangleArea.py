#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    try:
        b = input("Enter magnitude of Triangle base:")
        h = input("Enter Magnitude of Triangle Height:")
        a = (float(b) * float(h)) / 2
        print("Area of a Triangle with Height " + str(h) + " and Base "+ str(b) + " is " + str(a))
        break
    except:
        print("Base and Height should be numberic")


# In[ ]:




