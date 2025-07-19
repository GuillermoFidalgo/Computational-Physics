#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import sphere,vec,color
R=.3
m=2
x=0
for i in range(-m,m+1):
    for j in range(-m,m+1):
        for k in range(-m,m+1):

            if x%2==0:
                sphere(radius=R,pos=vec(i,j,k),color=color.white)
            else:
                sphere(radius=R,pos=vec(i,j,k),color=color.red)
            x+=1
