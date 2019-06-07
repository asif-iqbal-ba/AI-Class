#!/usr/bin/env python
# coding: utf-8

# In[112]:


# n is used for outer most loop
# p may be Integer or Any Special Character for print
# but when want to print sequance in pyramid pattern n and p always be equal
# h is used for half pyramid 1 for top to bottom 2 for bottom to top and 3 for full pyramid
# s is used when user draw pattern like below

def create_pattern(n, p, h, s):
    n=n;
    myp = p
    if int(h) == 1 or int(h) == 3:        
        for i in range(int(n) + 1):
            #print(str(i) + " I here")
            for j in range(i):
                try:
                    if int(p) > 0:
                        if int(s) == 1:
                            myp = i
                        else:
                            myp =  j + 1
                        #p = myp
                        #print(myp)
                        #myp = p - ()
                        #print(str(i) + " Inner Loop I")
                except:
                    p = p
                    #print("Ex")
                #p = p - 1                
                if int(s) != 1:
                    print (str(myp) + ' ', end="")                
                else:
                    print (str(myp), end="")
            print('')
    if int(h) == 2 or int(h) == 3:
        if int(h) == 3:
            n = int(n) - 1
        for i in range(n,0,-1):
            for j in range(i):
                try:
                    if int(p) > 0:
                        if int(s) == 1:
                            myp = i
                        else:
                            myp = j + 1
                except:
                    p = p
                    #print("Ex2")
                if int(s) != 1:
                    print(str(myp) + ' ', end="")
                else:
                    print (str(myp), end="")
            print('')
#create_pattern(5,  "*", 3, 1)
mybool = True
while mybool == True:
    try:
        n = input("Please Enter a Number of Rows Here :")
        p = input("Please Enter Pettern Value may be Integer or special character like * ")
        h = input("Please Enter Patten 1 is for top to bottom 2 is used for bottom to top and 3 is for Full pyramid:" )
        s = input("Enter 1 for Numbers Recursion")
        create_pattern(n, p, h, s)
        #print("Reach")
        break
    except:
        print("Provide Right values and Try Again")


# In[ ]:





# In[ ]:




