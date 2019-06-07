#!/usr/bin/env python
# coding: utf-8

# In[4]:


while True:
    x1 = input("Enter Co-ordinate for x1: ")
    y1 = input("Enter Co-ordinate for y1: ")
    x2 = input("Enter Co-ordinate for x2: ")
    y2 = input("Enter Co-ordinate for x1: ")
    try:
        d = pow(pow(float(x2) - float(x1), 2) +  pow(float(y2) - float(y1), 2), 1/2)
        print("Result :---Distance between points (" + str(x1) + "," + str(y1) + ") and (" + str(x2) + "," + y2 + ") is " + str(d))
        break
    except:
        print("Please enter all values in Numeric or Integer")
        #break


# In[ ]:




