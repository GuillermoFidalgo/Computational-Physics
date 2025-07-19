#!/usr/bin/env python
# coding: utf-8

#  Importando módulos

# In[1]:


import numpy as np


# In[2]:


# inicializando parámetros
m = 9.11e-31
h=6.626e-34
hbar=h/(2*np.pi)
E=10 #eV
V= 9 #eV


# Definimos los números de onda 
# \begin{gather}
# k_1=\frac{\sqrt{2mE}}{\hbar} \\
# k_2=\frac{\sqrt{2m(E-V)}}{\hbar}
# \end{gather}

# In[3]:


k1=np.sqrt(2*m*E)/hbar
k2=np.sqrt(2*m*(E-V))/hbar


# Definimos la probabilidad de transmisión y reflexión
# 
# $$ T = \frac{4k_1 k_2}{(k_1 + k_2)^2} \hspace{2cm} R=\left(\frac{k_1 - k_2}{k_1 + k_2}\right)^2$$

# In[4]:


T= 4*k1*k2/(k1+k2)**2
R= ((k1-k2)/(k1+k2))**2


# In[5]:


print("La probabilidad de transmisión es {} \ny la probabilidad de reflexión es {}".format(T,R))

