#!/usr/bin/env python
# coding: utf-8

# In[5]:


#from datetime import date
import datetime
def days_in_twodate(dta, dtb):
    d1 = datetime.datetime.strptime(dta,  "%d/%m/%Y")
    d2 = datetime.datetime.strptime(dtb,  "%d/%m/%Y")
    return abs((d2 - d1).days)
#from datetime import time
#x = datetime.datetime.now()
#x = datetime.datetime.strptime("12/12/2018", "%d/%m/%Y")
#print(days_in_twodate("12/12/2018", "16/12/2018"))
while True:
    try:
        d1 = input("Enter a date in (dd/mm/yyyy) format:")
        d2 = input("Enter a greater date from previous date in (dd/mm/yy) format:")
        print("There are " + str(days_in_twodate(d1, d2)) + " days between " + d1 + " and " + d2 )
        break
    except:
        print("Please Enter valid dates in Required Format")


# In[ ]:




