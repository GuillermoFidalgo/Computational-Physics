#!/usr/bin/env python
# coding: utf-8

# ![exercise1](images/ex1.png)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# # Partes a) y b)

# In[2]:


def Binding_energy(A,Z,ret="b"):
    #Todos están en MeV
    a1=15.8
    a2=18.3
    a3=0.714
    a4=23.2
    #si A es impar
    if A%2 ==1:
        a5= 0

    #si A y Z son par
    elif A%2 ==0 and Z%2 ==0 :
        a5=12

    #Si A es par y Z es impar
    elif A%2==0 and Z%2==1:
        a5=-12


    B= a1*A - a2*A**(2/3) - a3*(Z**2/A**(1/3)) - a4*((A-2*Z)**2)/A + a5/(A**.5)


    if ret == "b":
        return B
    elif ret == "b/a":
        return B/A



# In[3]:


print('Energía de enlace es {} MeV'.format(Binding_energy(58,28)))


# In[4]:


print('Energía de enlace por nucleón es {} MeV'.format(Binding_energy(58,28,ret='b/a')))


# # Parte c)

# In[5]:


Z=int(input('Ingrese número atómico\n'))
A = np.arange(Z,3*Z+1)


# In[6]:


maxBindE=0
for a in A:
    if Binding_energy(a,Z,ret='b/a') > maxBindE:
        maxBindE=Binding_energy(a,Z,ret='b/a')
        MaxA=a

print("El número de masa A={0} tiene la mayor energía por nucleón : {1} MeV".format(MaxA,maxBindE))


# # Parte d)

# In[7]:


Z=np.arange(1,101)
MAXbindEnergies=[]
MAX_A=[]

for z in Z:

    maxBindE=0

    for a in np.arange(z,3*z+1):
        if Binding_energy(a,z,ret='b/a') > maxBindE:
            maxBindE=Binding_energy(a,z,ret='b/a')
            MaxA=a
    MAXbindEnergies.append(maxBindE)
    MAX_A.append(MaxA)


    print("El número atómico Z={0} tiene la mayor energía por nucleón cuando A={1}\n con energía {2}\n\n"
          .format(z,MaxA,maxBindE))


# In[8]:


Z_max_index= np.argmax(MAXbindEnergies)
print("Z={} tiene el valor máximo de B/A con A = {} y B/A={} MeV"
      .format(Z[Z_max_index],MAX_A[Z_max_index],MAXbindEnergies[Z_max_index]))
