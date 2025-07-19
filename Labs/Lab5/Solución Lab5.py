#!/usr/bin/env python
# coding: utf-8

# ![problem](problem.png)

# In[1]:


from numpy import array


# \section*{a)}

# In[2]:


a=float(input('ingrese coeficiente "a" de la cuadrática'))
b=float(input('ingrese coeficiente "b" de la cuadrática'))
c=float(input('ingrese coeficiente "c" de la cuadrática'))


# In[16]:


def quadratic(a,b,c):
    pm=array([+1,-1])
    x = -b + pm*(b**2 - 4*a*c)**.5
    x= x/(2*a)
    return x


# In[17]:


x= quadratic(a,b,c)
print(x)


# \section*{b)}

# In[18]:


def quadratic2(a,b,c):
    pm=array([+1,-1])
    x = -b - pm*(b**2 - 4*a*c)**.5
    x= (2*c)/x
    return x


# In[19]:


x = quadratic2(a,b,c)
print(x)


# Observamos que este método solamente provee la primera raíz (el número pequeño) con el valor correcto mientras que para el primer método se devuelve la segunda raíz (el número grande) con el valor correcto.

# Esto se explica con que el primer método trabaja bien calculando números grandes pero el segundo método trabaja bien para calcular números pequeños. Esto es debido a errores de redondeo para cada método.

# \section*{c)}

# In[20]:


def quadratic_adj(a,b,c):
    x=quadratic(a,b,c)[1],quadratic2(a,b,c)[0]
    return x


# In[21]:


x=quadratic_adj(a,b,c)
print(x)

