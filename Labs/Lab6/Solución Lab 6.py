#!/usr/bin/env python
# coding: utf-8

# ![problem](images/problem.png)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.serif": ["Palatino"],
})


# \section*{a)}

# In[2]:


def f(x):
    return x*(x-1)
x=1
delta=1e-2
dydx=(f(x+delta)-f(x))/delta
print(dydx)


# El valor analítico de la derivada de la función $f(x)= x(x-1)$ evaluado en x=1 es 
# $$ f'(x)= \frac{d}{dx} (x^2-x)= 2x -1$$
# $$ \boxed{f'(1)= 2(1) -1 = 1} $$
# Si comparamos esto dos números obtenemos que están a $1\%$ de diferencia

# In[3]:


abs(1-1.010000000000001)*100


# Estos no coninciden porque por la definición de límites de la derivada estamos insertando un número finito en la $\delta=0.01$ y no se está tomando el límite cuando $\delta \to 0$. En teoría esto produce el resultado exacto pero numéricamente, por limitaciones de la computadora no se puede hacer $\delta =0$.

# section*{b)}

# In[4]:


delta=np.array([1e-2,1e-4,1e-6,1e-8,1e-10,1e-12,1e-14])
dydx=(f(x+delta)-f(x))/delta
err=abs(dydx-1)
for i in dydx:
    print(" dy/dx \t\t\t\t error (absoluto) \t\t error (porcentual) ")
    print(" {} \t \t {} \t\t  {:%}".format(i,abs(i-1),abs(i-1)))
    print('')
# print(err)


# In[5]:


plt.figure(dpi=290)
plt.plot(delta,err,'o--')
plt.yscale('log')
plt.xscale('log')
plt.title("Error vs $\delta$",size=18)
plt.grid()
plt.xlabel('$\delta$',size=14)
plt.ylabel("error \n(absolute)",rotation =0,labelpad=28,size=12)
plt.show()


# La razón por la que se observa este comportamiento es por que se llegan a las límitaciones de las computadoras en cuanto a su precisión finita. Cuando  $\delta< 10^{-8}$ se está tomando restas entre número muy cercanos y se divide por un número de orden menor a $ 10^{-8}$.
