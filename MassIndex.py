#!/usr/bin/env python
# coding: utf-8

# In[4]:


while True:
    try:
        height = input("Enter Height in Meter here: ")
        weigh = input("Enter Weight in Kg here: ")
        massindex = float(weigh) / pow(float(height), 2)
        #print("here")
        print("Your BMI is " + str(massindex) + " Kg/sq.Meter with Weight " + str(weigh) +" in " + str(height) + " meter Height")
        break
    except:
        print("Enter All values in Numeric")
        #break


# In[ ]:




