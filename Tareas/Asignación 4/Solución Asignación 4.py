#!/usr/bin/env python
# coding: utf-8

# ![problem1](problem1.png)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "sans-serif",
#     "font.sans-serif": ["Helvetica"]})
# for Palatino and other serif fonts use:
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})


# \section*{a)}

# In[2]:


k_B=1.38064852e-23
def f(x):
    func=x**4*np.exp(x)/(np.exp(x)-1)**2
    return func



def cv(T,V=0.001,rho=6.022e28,theta_D=428,N=1000):
    constantes=9*V*rho*k_B*(T/theta_D)**3
    a=0
    b=theta_D/T
    h=(b-a)/N
    fa=0
    fb=.5*f(b)
    integral=0
    for k in range(1,N):
        integral=f(a+k*h)+integral
    integral=integral+ .5*fa + .5*fb
    C_v=constantes*integral*h
    return C_v


# \section*{b)}

# In[3]:


T=np.arange(5,500)
Cv=[cv(x) for x in T]


# In[5]:


plt.figure(dpi=250)
plt.plot(T,Cv)
plt.title(r"$C_v$ vs $T$",size=16)
plt.xlabel("$T$",size=12)
# plt.yscale("log")
plt.ylabel("$C_v$",size=12,rotation=0,labelpad=13)
# plt.savefig("figure1.png",dpi=250)
plt.show()


# \newpage

# ![problem2](problem2.png)

# section*{a)}

# In[5]:


def f(x):
    func=x**4-2*x+1
    return func

def simp(func,N=10,a=0,b=2):
    h=(b-a)/N
    fa=f(a)
    fb=f(b)
    integral=0
    for k in range(1,N,2):
        integral=4*f(a+k*h)+integral
    for k in range(2,N-1,2):
        integral=2*f(a+k*h)+integral
        
    integral=(1/3)*h*(integral+fa+fb)
    I=integral
    return I


# \section*{b)}

# In[6]:


I_simp=simp(f)

error= (I_simp-4.4)/4.4
print("El error fraccionario es de :",error)
print("En porciento es de {:.4%}".format(error))


# \section*{c)}

# In[7]:


I_simp100= simp(f,N=100)
I_simp1000= simp(f,N=1000)


# In[9]:


print(I_simp100,I_simp1000)
error100= (I_simp100-4.4)/4.4
error1000=(I_simp1000-4.4)/4.4
print("Sus errores son de {:.6%} y {:.10%} respectivamente".format(error100,error1000))


# Estos resultados son órdenes de magnitud más precisos que al utilizar el método del trapezoide.
