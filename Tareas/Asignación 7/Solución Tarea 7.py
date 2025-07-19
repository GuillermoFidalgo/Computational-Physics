#!/usr/bin/env python
# coding: utf-8

# ![problem](problem.png)

# \section*{a)}

# Sabemos que por la la ley de corriente de Kirchhoff, la suma de las corrientes en una malla debe ser 0. Ya tenemos la ecuacion para la unión a voltaje $V_1$, asi que para el resto tenemos:
# \begin{align}
# &\frac{V_2 - V_1}{R} + \frac{V_2 }{R} + \frac{V_2 - V_4}{R}=0 & \to &&   - V_1 +  3V_2 - V_4=0\\
# &\frac{V_3 - V_1}{R}+\frac{V_3 - V_4}{R}+\frac{V_3 - V_+}{R}=0 & \to &&  - V_1 +3V_3- V_4 =V_+\\ 
# &\frac{V_4 - V_1}{R}+\frac{V_4 - V_2}{R}+\frac{V_4 }{R}+\frac{V_4 - V_3}{R}=0  & \to  && -V_1 - V_2 - V_3 +4V_4=0\\
# \end{align}

# In[1]:


from numpy import array,empty,copy
import numpy as np


# In[2]:


def gausselim(A,v,N,pivot=False):
    
        
    # Gaussian elimination
    for m in range(N):
        #pivoting
        if pivot == True:
            if A[m,m]==0:
                B=copy(A)
                maxm= np.max(abs(B),axis=0)
                maxi=np.argmax(maxm)
                A[m,:],A[maxi,:]=B[maxi,:],B[m,:]
                v2=copy(v)
                v[m],v[maxi]=v2[maxi],v2[m]

        # Divide by the diagonal element            
        div = A[m,m]
        A[m,:] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult = A[i,m]
            A[i,:] -= mult*A[m,:]
            v[i] -= mult*v[m]

    # Backsubstitution
    x = empty(N,float)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i]

    return x


# \section*{b)}

# In[3]:


A = array([[ 4, -1, -1, -1 ],
           [ -1, 3,  0, -1 ],
           [ -1, 0,  3, -1 ],
           [ -1, -1, -1, 4 ]],float)
v= array([5 , 0 ,5 ,0],float)
N = len(v)
print("A= \n",A)
print("\nv =",v)


# In[4]:


x=gausselim(A,v,N)
print("El vector x es \nx=",x)


# ![problem2](problem2.png)

# \section*{a)}

# In[5]:


A = array([[ 4, -1, -1, -1 ],
           [ -1, 3,  0, -1 ],
           [ -1, 0,  3, -1 ],
           [ -1, -1, -1, 4 ]],float)
v= array([5 , 0 ,5 ,0],float)
N = len(v)
print("A= \n",A)
print("\nv =",v)


# In[6]:


x=gausselim(A,v,N,pivot=True)
print("x con pivot\n",x)


# \section*{b)}

# Ecuación 6.17 es
# $$
# \begin{pmatrix}
# 0 & 1 & 4 & 1\\ 
# 3 & 4 & -1 & -1 \\
# 1 & -4 & 1 & 5 \\
# 2 & -2 & 1 & 3
# \end{pmatrix}
# \begin{pmatrix}
# w \\ x \\ y \\z
# \end{pmatrix}
# = 
# \begin{pmatrix}
# -4 \\ 3 \\ 9 \\7
# \end{pmatrix}
# $$

# In[7]:


A = array([[ 0, 1, 4, 1 ],
           [ 3, 4,-1,-1 ],
           [ 1,-4, 1, 5 ],
           [ 2,-2, 1, 3 ]],float)
v= array([-4 , 3 ,9 ,7],float)
N = len(v)
print("A= \n",A)
print("\nv =",v)


# In[8]:


x=gausselim(A,v,N,pivot=True)
print("x con pivot\n",x)


# ![problem3](problem3.png)

# In[9]:


A = array([[ 4, -1, -1, -1 ],
           [ -1, 3,  0, -1 ],
           [ -1, 0,  3, -1 ],
           [ -1, -1, -1, 4 ]],float)
v= array([5 , 0 ,5 ,0],float)
N = len(v)
print("A= \n",A)
print("\nv =",v)


# In[10]:


from numpy.linalg import solve 
x = solve(A,v) 
print("x con solve\n",x)

