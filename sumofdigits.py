#!/usr/bin/env python
# coding: utf-8

# In[8]:


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
        # print(s)
        # print(n)
    return s
# i = 0
n = 0
mybool = True
while mybool == True:
    try:
        # i +=1
        # print(i)
        n = input("Enter Number here or q for Quit: ")
        if n != "q":
            sum_n = sum_digits(int(n))
            print("Sum of digits of number " + str(n) + " is " + str(sum_n))
            # break
        # n = input("Enter Another Number to check or q for Q")
        if n == "q":
            mybool = False
    except:
        print("Enter value in Numeric")    
        #break


# In[ ]:




