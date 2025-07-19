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

# In[8]:


from numpy import array,empty
def gausselim(A,v,N):

    # Gaussian elimination
    for m in range(N):

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


# In[17]:


A = array([[ 4, -1, -1, -1 ],
           [ -1, 3,  0, -1 ],
           [ -1, 0,  3, -1 ],
           [ -1, -1, -1, 4 ]],float)
v= array([5 , 0 ,5 ,0],float)
N = len(v)


# In[18]:


x=gausselim(A,v,N)

