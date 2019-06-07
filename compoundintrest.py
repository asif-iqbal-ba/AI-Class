#!/usr/bin/env python
# coding: utf-8

# In[3]:


while True:
    p_amount = input("Enter Principle Amount: ")
    i_rate = input("Enter Intrest Rate in percentage Here: ")
    y_year = input("Enter No of Years Here: ")
    try:
        a = float(p_amount) * (pow(1 + float(i_rate)/100, float(y_year)))
        print("After " + y_year + " years your principal amount "+ p_amount + " over an interest rate of " + i_rate + " % will be " + str(a))
        break
    except:
        print("Please Enter valid values in Numeric forms form Principle Amount, Rate and years")
        
        


# In[ ]:




