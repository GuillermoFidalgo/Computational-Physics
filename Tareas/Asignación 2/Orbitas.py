
# ![ex2](images/ex2.png)

# # Parte a)

# Comenzando con la ecuación cuadrática
# \begin{gather*}
# v_2^2 - 2\frac{GM}{v_1\ell_1}v_2 - \left[ v_1^2 - \frac{2GM}{\ell_1} \right]=0\\
# v_2 = \frac{\frac{2GM}{v_1 \ell_1} \pm \sqrt{(2GM/v_1 \ell_1)^2 - 4(1)(-v_1^2 + \frac{2GM}{\ell_1})}}{2}\\
# v_2 = \frac{GM}{v_1 \ell_1} \pm \sqrt{\left(\frac{2GM}{v_1 \ell_1}\right)^2 + \frac{4(v_1^2 \ell_1 - 2GM)v^2_1 \ell_1}{(v_1 \ell_1)^2}}\\
# v_2 = \frac{GM}{v_1 \ell_1} \pm \frac{2\sqrt{(GM)^2 -2(GM)v_1^2\ell_1 + (v_1^2\ell_1)^2}  }{2v_1\ell_1}\\
# v_2= \frac{GM}{v_1 \ell_1} \pm \frac{\sqrt{(GM-v_1^2\ell_1)^2}}{v_1 \ell_1}\\
# v_2 =  \frac{GM}{v_1 \ell_1} \pm \left(\frac{GM}{v_1\ell_1} - v^2_1 \ell_1\right)
# \end{gather*}

# Si tomamos el valor $(+)$ obtenemos que

# $$v_2= \frac{GM}{v_1 \ell_1} + \frac{GM}{v_1\ell_1} - v^2_1 \ell_1= 2\frac{GM}{v_1\ell_1} -v_1 $$
# Si tomamos el valor $(-)$ obtenemos
#
# $$v_2= \frac{GM}{v_1 \ell_1} - \frac{GM}{v_1\ell_1} + v^2_1 \ell_1= v_1 $$

# El problema con este segundo resultado es que sabemos que  por la segunda Ley de Kepler, la velocidad en afelio debe ser menor que la velocidad en perihelio $(v_2 < v_1)$ por lo tanto el término menor es el término $(+)$ con
# $$v_2 = 2\frac{GM}{v_1\ell_1} -v_1$$

# # Parte b) y c)
# ## Valores para la Tierra

# In[9]:


#Definimos los parámetros
# v1=3.0287e4
# l1=1.4710e11
M= 1.9891e30 #Kg
G= 6.6738e-11
v1=float(input("Ingrese velocidad en perihelio\n"))
l1=float(input("Ingrese distancia en perihelio\n"))


# Calculamos $v_2,\ell_2,T$ y $e$

# In[10]:


v2 = 2*G*M/(v1*l1) - v1
l2 = l1*v1/v2
a=.5*(l1+l2)
b= (l1*l2)**.5
T=2*np.pi*a*b/(l1*v1)/(3600*24*365) # days
e=(l2-l1)/(l2+l1)


# In[11]:


print("Para la tierra\nl2 = {:,} m\nv2 = {:,} m/s\nT = {:,} años\ne = {:,}".format(l2,v2,T,e))


# ## Para el cometa Halley

# In[12]:


# v1=5.4529e4
# l1=8.7830e10

v1=float(input("Ingrese velocidad en perihelio\n"))
l1=float(input("Ingrese distancia en perihelio\n"))


# In[13]:


v2 = 2*G*M/(v1*l1) - v1
l2 = l1*v1/v2
a=.5*(l1+l2)
b= (l1*l2)**.5
T=2*np.pi*a*b/(l1*v1)/(3600*24*365) # days
e=(l2-l1)/(l2+l1)


# In[15]:


print("Para el cometa Halley\nl2 = {:,} m\nv2 = {:,} m/s\nT = {:,} años\ne = {:,}".format(l2,v2,T,e))
