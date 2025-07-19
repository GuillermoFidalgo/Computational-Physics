#!/usr/bin/env python
# coding: utf-8

# ![problem1](Problem1.png)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (np.sin((100*x)**.5))**2
    
def trapezoid(f,a=0,b=1,h=1,N=1):
    h=(b-a)/N
    s = 0.5*f(a) + 0.5*f(b)
    for k in range(1,N):
        s += f(a+k*h)
    return h*s


# \section*{a)}

# In[2]:


N = 1 # Número inicial de pasos 
a=0
b=1
h=(b-a)/N
I=[]
k =0

epsilon,err= 1e-6,1

I.append(trapezoid(f,N=1)) # valor inicial $I_1$
print("N = {:4}\t I = {:.7f}\t error = N/A".format(N,I[0]))

while abs(err) > epsilon:
    N=2*N
    h = h/2
    s=0
    for n in range(1,N,2):
        s+= f(a+n*h)
    i= .5*I[k] + h*s
    I.append(i)
    k+=1
    err =  (I[k] - I[k-1])/3    
    print("N = {:4}\t I = {:.7f}\t error = {:.7f}".format(N,i,err))


# \section*{b)}

# In[3]:


def romberg(f,a,b,h,N,precision=1e-6):
    R=[]
    I1=trapezoid(f,a,b,h,N)
    R.append([I1])
    ERR=[]
    err=1
    i=1
    while abs(err) > precision:
        N=2*N
        h=h/2
        s=0
        for n in range(1,N,2):
            s+= f(a+n*h)
        I_1m= .5*I1 + h*s
        R.append([I_1m])
        I1=I_1m
        
        
        for m in range(1,i+1):
            err= (1/(4**m-1))*(R[i][m-1] - R[i-1][m-1])
            ERR.append(err)
            R_im= R[i][m-1] + err
            R[i].append(R_im)
        i+=1
        
    return R,ERR,N


# In[4]:


N=1
a=0
b=1
h=(b-a)/N

r=romberg(f,a,b,h,N)


for i in r[0]:
    print(i)
print("\nN = {} steps".format(r[2]))


# ![problem1](Problem2.png)

# In[5]:


def adap_simp(f,a=0,b=1,N=2,h=.5):
    fa=f(a)
    fb=f(b)
    integral=0
    
    for k in range(2,N-1,2):
        integral=f(a+k*h)+integral
    
    S=(integral*2 + fa+fb)*(1/3)
    
    
    integral=0
    for k in range(1,N,2):
        integral=f(a+k*h)+integral
    T=integral*(2/3)
    
    
    integral=h*(S+2*T)
    I=integral
    return I,S,T


# In[24]:


N=2
h=.5
a=0
b=1

I,S,T=adap_simp(f,N=N,h=h,a=a,b=b)
err = 1
tol=1e-6
print("I = {:.7f}\t N= {}\t error is {:.7f}".format(I,N,err))
while abs(err)>tol:
    
    N=2*N
    h=h/2
    S=S+T
    _,_,T=adap_simp(f,a,b,h=h,N=N)

    Inew = h*(S+2*T)
    
    err=(1/15)*(Inew-I)
    I=Inew
    print("I = {:.7f}\t N= {}\t error is {:.7f}".format(I,N,err))


# In[ ]:




