#!/usr/bin/env python
# coding: utf-8

# La distancia que entre la tierra y planeta es x

# In[1]:


x=float(input("Entre la distancia de la tierra en años luz\n"))
v=float(input("Entre la velocidad del cohete como fracción de c\n"))


# Para el observador en la tierra el tiempo de vuelo es calculado simplemente con 
# 
# $$ t=\frac{x}{v}$$

# In[2]:


t=x/v
print("El tiempo de vuelo para un observado en tierra es",t)


# Para un observador en el cohete el tiempo de vuelo es 
# $$ t = \gamma t_0$$
# donde $$\gamma =\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}$$
# con $c=1$ tenemos

# In[3]:


gamma = 1/((1-v**2)**.5)
t0=t/gamma
print("El tiempo de vuelo para un observador en el cohete es {} años luz".format(t0))

