#!/usr/bin/env python
# coding: utf-8

# ![ejercicio](images/lab4.png)

# \section*{Parte a)}

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


data=np.loadtxt('sunspots.txt')
time=data[:,0]
numspots=data[:,1]


# In[3]:


plt.figure(dpi=500,figsize=(12,4))
plt.plot(time,numspots)
plt.xlabel('Months')
plt.ylabel('# of Sunspots')
plt.show()


# \section*{Parte b)}

# In[4]:


plt.figure(dpi=500,figsize=(12,4))
plt.plot(time[:1000],numspots[:1000])
plt.xlabel('Months')
plt.ylabel('# of Sunspots')
plt.show()


# \section*{Parte c)}

# In[5]:


# Calculando el running average
def runingAvg(y,r=5):
    Y=[]
    for k in range(len(y)):
        avg=0
        if k>=r and k < len(y)-r:
            for m in range(-r,r+1,1):
                avg=(.5/r)*(y[k+m])+avg
            Y.append(avg)
    return Y


# In[6]:


RunAvg=runingAvg(numspots,r=5)


# In[7]:


plt.figure(dpi=500,figsize=(12,4))
plt.plot(time[:1000],numspots[:1000])
plt.plot(time[:1000],RunAvg[:1000])
plt.xlabel('Months')
plt.ylabel('# of Sunspots')
plt.show()
