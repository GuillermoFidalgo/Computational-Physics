#!/usr/bin/env python
# coding: utf-8

# # a)

# In[21]:


import numpy as np
import matplotlib.pyplot as plt


# In[22]:


theta=np.linspace(0,2*np.pi)
x=2*np.cos(theta)+np.cos(2*theta)
y=2*np.sin(theta)-np.sin(2*theta)


# In[23]:


plt.figure(dpi=200)
plt.plot(x,y)
plt.show()


# # b)

# In[58]:


theta=np.linspace(0,10*np.pi)
r=theta**2

x=r*np.cos(theta)
y=r*np.sin(theta)


# In[59]:


plt.figure(dpi=200)
plt.plot(x,y)
plt.show()


# # c)

# Aquí mostramos la gráfica de la función de Fey transformada a coordenadas cartesianas

# In[79]:


theta=np.linspace(0,24*np.pi,1000)
r=np.exp(np.cos(theta))-2*np.cos(4*theta)+np.sin(theta/12)**5

x=r*np.cos(theta)
y=r*np.sin(theta)
plt.figure(dpi=200)
plt.plot(x,y)
plt.show()


# Aquí tenemos la gráfica polar de la función de Fey

# In[80]:


plt.figure(dpi=200)
plt.polar(theta,r)
plt.show()

