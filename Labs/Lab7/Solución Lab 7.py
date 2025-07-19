#!/usr/bin/env python
# coding: utf-8

# ![problem](problem.png)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# \section*{a)}

# In[8]:


data=np.loadtxt("velocities.txt")
t=data[:,0]
vx=data[:,1]


# In[73]:


def f(x):
    return vx[x]

N = len(vx)
a = 0
b = 100
h = 1
pos=[]
s = 0.5*f(a) + 0.5*f(b)
pos.append(h*s)
for k in range(1,N):
    s += f(a+k*h)
    pos.append(h*s)


# \section*{b)}

# In[85]:


plt.figure(dpi=150)
plt.plot(t,vx,label='velocity')
plt.plot(t,pos,label='position')
plt.xlabel("time",size=12)
plt.ylabel("Velocity\nand\nPosition",size=12,labelpad=30,rotation=0)
plt.tight_layout()
plt.legend()
plt.show()


# In[ ]:




