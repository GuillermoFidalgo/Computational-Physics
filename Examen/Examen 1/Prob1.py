#!/usr/bin/env python
# coding: utf-8

# \section*{a)}

# Si tenemos que 
# $$I(\omega)= \frac{\hbar}{4\pi^2 c^2}\frac{\omega^3}{(e^{\hbar \omega / k_B T}-1)}$$

# Entonces la energía total por unidad de área es $W=\int I (\omega) d\omega$. 
# 
# \begin{gather*}
# W =\frac{\hbar}{4\pi^2 c^2}\int_0^\infty \frac{\omega^3}{(e^{\hbar \omega / k_B T}-1)} d\omega
# \end{gather*}

# hacemos la susitución $$x= \frac{\hbar \omega }{ k_B T} \to \omega=\frac{k_B T }{\hbar}x$$ y
# $$ dx = \frac{\hbar}{k_B T}d\omega \to d\omega = \frac{k_B T }{\hbar} dx$$

# y obtenemos que 
# \begin{gather*}
# W =\frac{\hbar}{4\pi^2 c^2}\int_0^\infty \frac{(k_B T/\hbar)^3 x^3}{(e^{x}-1)} (k_B T/\hbar)dx \\
# W= \frac{k_B^4 T^4}{4\pi^2 c^2\hbar^3}\int_0^\infty \frac{x^3}{(e^{x}-1)} dx
# \end{gather*}
# 
# 

# \section*{b)}

# Tomamos los códigos para [cuadratura de gauss](http://www-personal.umich.edu/~mejn/cp/programs/gaussxw.py) provista por el libro  y para [integración impropia](http://www-personal.umich.edu/~mejn/cp/programs/intinf.py)

# In[28]:



from numpy import ones,copy,cos,tan,pi,linspace,exp,array,pi

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w


# Cambiamos de variable para que la integral ahora sea de la siguiente forma
# \begin{gather*}
# W= \frac{k_B^4 T^4}{4\pi^2 c^2\hbar^3}\int_0^\infty \frac{x^3}{(e^{x}-1)} dx\\
# = \frac{k_B^4 T^4}{4\pi^2 c^2\hbar^3}\int_0^1 \frac{z^3/(1-z)^3}{(e^{(z/(1-z)}-1)} \frac{1}{(1-z)^2} dz = \frac{k_B^4 T^4}{4\pi^2 c^2\hbar^3}\int_0^1 \frac{z^3}{(e^{(z/(1-z)}-1)} \frac{1}{(1-z)^5} dz
# \end{gather*}
# 

# Solo evaluamos el integrando de la expresión (sin incluir las constantes)

# In[29]:



#cambiamos de variable nuestra función en terminos de z

def f(z):
    return ((z)**3/(exp(z/(1-z))-1))*(1/(1-z)**5)

def integrate(f,a,b,N):
    x,w = gaussxwab(N,a,b)
    s = 0.0
    for k in range(N):
        s += w[k]*f(x[k])
    return s


# In[30]:


Err=[]
for i in range(1,31):
    I1=integrate(f,a=0.0,b=1.0,N=i)
    I2=integrate(f,a=0.0,b=1.0,N=i+1)
    Err.append(abs(I2-I1))
    print("error es {:2.1e}  valor de integral es {:9.6f} con N={}".format(abs(I2-I1),I1,i))
# print("Valor de integral es",I1,"con N=%i" %i)


# Dejándonos llevar por nuestro estimado del error pienso que el error es del orden $1\times 10^{-6}$ con $N=30$

# \section*{c)}

# Estimando la constante $\sigma$ de Stefan-Boltzmann utilizando $W=\sigma T^4$.
# Si igualamos ambas ecuaciónes y comparamos tenemos que 
# $$\sigma T^4 = \frac{k_B^4 T^4}{4\pi^2 c^2\hbar^3}\int_0^1 \frac{z^3}{(e^{(z/(1-z)}-1)} \frac{1}{(1-z)^5} dz$$

# y por lo tanto $\sigma$ debería ser $$\sigma=\frac{k_B^4}{4\pi^2 c^2\hbar^3}\int_0^1 \frac{z^3}{(e^{(z/(1-z)}-1)} \frac{1}{(1-z)^5} dz$$

# In[35]:


Int=integrate(f,a=0.0,b=1.0,N=30)
kB=1.38e-23
c=3e8
hbar=6.626e-34/(2*pi)


# In[36]:


sigma = kB**4/(4*pi**2 * c**2 * hbar**3)


# In[44]:


print("sigma={:.3e}".format(sigma))

