#!/usr/bin/env python
# coding: utf-8

# ![](problem.png)

# \section*{a)}

# Tenemos que diferenciar la ecuación $$ I(\lambda)= \dfrac{2\pi h c^2 \lambda^{-5}}{e^{hc/\lambda k_B T} -1 }$$

# \begin{align}
# \dv{I(\lambda)}{\lambda}=&\dv{\lambda}(\dfrac{2\pi h c^2 \lambda^{-5}}{e^{hc/\lambda k_B T} -1 })= 0 \\
# =&2\pi h c^2 \dv{\lambda}(\frac{\lambda^{-5}}{e^{hc/\lambda k_B T} -1 })=0\\
# =&2\pi h c^2 \left(-5\lambda^{-6} (e^{hc/\lambda k_B T} -1)^{-1} + \lambda^{-5}(e^{hc/\lambda k_B T} -1)^{-2} e^{hc/\lambda k_B T}\frac{hc}{\lambda^2 k_B T} \right) =0\\
# =& \left(-5 + \frac{e^{hc/\lambda k_B T} }{e^{hc/\lambda k_B T} -1}\frac{hc}{\lambda k_B T} \right)=0\\
# =& \frac{-5 e^{-hc/\lambda k_B T} (e^{hc/\lambda k_B T} -1) + hc/\lambda k_B T}{e^{hc/\lambda k_B T} -1}=0\\
# =& 5 e^{-hc/\lambda k_B T}  + \frac{hc}{\lambda k_B T} -5=0
# \end{align}

# Ahora hacemos la sustitución $ x = \dfrac{hc}{\lambda k_B T}$ y despejamos para $ \lambda$ 
# \begin{gather*}
# x = \frac{hc}{\lambda k_B T} \to
# \lambda = \frac{hc}{xk_B T}
# \end{gather*}
# Si $ b = \dfrac{hc}{xk_B}$ entonces 
# $$ \lambda = \frac{b}{T}$$

# \section*{b)}

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# Para la función $f(x)=5 e^{-x} +x -5 $

# In[2]:


def f(x):
    return 5*np.exp(-x)+x - 5


def binary_search(f,a,b,acc=1e-6):
    err=1
    if f(a)*f(b) <0:
        print("there is a root between {} and {}".format(a,b))
        while err> acc:      
            mid=(a+b)/2
            if f(mid)*f(a)>0:
                a=mid
            else:
                b=mid
            err=abs(a-b)
        return mid
        
    else:
        print("ERROR\nchoose other interval\n")
        return None
    
    


# Primero inspeccionamos el comportamiento de esta función para tener una idea de su comportamiento y un estimado de la raíz.

# Por inspección sabemos que una raíz debe ser $x=0$, dado que esta función cruza por el origen y sabemos que en el intevalo $x \in [0,\infty)$ el término $x-5$ domina la función así que esperaría que la segunda raíz debe estar cerca de $x=5$

# In[3]:


for a,b in zip([-1,-1,-1],[1,5,10]):
    x=np.linspace(a,b,100)

    plt.plot(x,f(x))
    plt.vlines(0,min(f(x)),max(f(x)),colors="k")
    plt.hlines(0,min(x),max(x),"k")
    plt.show()


# Vemos que hay 2 raíces donde anticipamos

# In[4]:


x1=binary_search(f,-1,1)
print("la primera raíz es x =",x1,"\nDebe ser 0\n")
x2=binary_search(f,4,6)
print("La segunda raíz es x =",x2)


# Determinamos ahora la constante de desplazameinto de Wein $  b = \dfrac{hc}{xk_B}$. Notamos que no tiene sentido utilizar la raíz $x=0$ por lo tanto tenemos que 

# In[5]:


h=6.626e-34
c=3e8
kB= 1.38e-23
A=h*c/kB

b= A/x2
print("la constante b es",b)


# \section*{c)}

# Estimamos la temperatura de la superficie del sol con la expresión $$\lambda = \frac{b}{T}\to T= \frac{b}{\lambda}$$

# In[6]:


lamda= 502e-9 #m
T = b/lamda
print("La temperatura superficial del Sol es",int(T),"K")

