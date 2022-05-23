#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Enter Total Number of Elements-\n")
n=int(input())
print("Enter Numbers-\n")
a=[]

for i in range(n):
    abc=int(input())
    a.append(abc)

output=len(a)
print(output)

for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_index]:
            min_index = j
    a[i] , a[min_index] = a[min_index],a[i]

a


# In[ ]:




