#!/usr/bin/env python
# coding: utf-8
# \begin{figure}[h]
# \includegraphics[width=\textwidth]{./images/Ball_drop.png}
# \end{figure}
# Importamos primero las librerías que necesitamos

# In[1]:


import numpy as np


# In[2]:


h=float(input("Entra una altura inicial:\n"))
# v0=0
g=9.81 #m/s^2


# Como nos interesa calcular el tiempo que tarda en llegar la bola al suelo partimos de la siguiente ecuación de cinemática
#
# $$ y= y_0 + v_0t -\frac{1}{2}gt^2$$

#  Sustituyendo que la velocidad inicial es 0 y que cuando la bola llega al suelo la altura final será 0, obtenemos la siguiente expresión para el tiempo de caída.
# \begin{gather*}
# 0= h  - \frac{1}{2}gt^2\\
# h= \frac12 gt^2 \\
# t= \sqrt{\frac{2h}{g}}
# \end{gather*}
#
# Ahora podemos calcular el tiempo de caída

# In[3]:


t=np.sqrt(2*h/g)
print('El tiempo de caída desde {}m es {}s'.format(h,t))


# \begin{figure}[h]
# \includegraphics[width=\textwidth]{./images/Satellite_altitude.png}
# \end{figure}

# \subsection*{a}
#

#
# Para mostrar esto primero partimos de la segunda ley de Newton para este sistema.
#
# \begin{align*}
#  F &= ma \\
# G\frac{Mm}{r^2} &= m\frac{v^2}{r}\\
# G\frac{M}{r} &= v^2
# \end{align*}
#

# Como el satélite está orbitando períodicamente cada $T$ segundos quiere decir que orbita a una frecuencia de
# \begin{gather*}
# \frac{v}{r}=\omega= 2\pi f= \frac{2\pi}{T}\\
# \therefore \; v=\frac{2\pi r}{T}
# \end{gather*}

# Sustituyendo esta expresión de $v$ en nuestra ecuación anterior obtenemos
# \begin{align*}
# G\frac{M}{r}&=\frac{4\pi^2 r^2}{T^2}\\
# r^3 &= G\frac{MT^2}{4 \pi^2}\\
# r &= \left(G\frac{MT^2}{4 \pi^2}\right)^{\frac13}
# \end{align*}

# Como $r$ es la distancia desde el centro de la tierra hasta el satélite tenemos entonces que $r= R +h$

# \begin{align*}
# R+h&= \left(G\frac{MT^2}{4 \pi^2}\right)^{\frac13}\\
# h &= \left(G\frac{MT^2}{4 \pi^2}\right)^{\frac13} -R
# \end{align*}

# \subsection*{b y c}

# In[60]:


from scipy.constants import G,pi,minute,hour,day
import sys
# minute,hour,day son los segundos que hay en un minuto,hora y día respectivamente

R=6371e3 # metros
M = 5.97e24 # kg


# In[61]:


for i in range(3):
    T=input("\nIngrese el periodo de orbita del satélite (con las unidades 's' 'min' o 'h') \n")
    if "s" in T:
        T=float(T.strip("s"))

    elif "min" in T:
        T=float(T.strip("min"))
        T=T*minute

    elif "h" in T:
            T=float(T.strip("h"))
            T=T*hour
    else:
        print('ingrese unidades al periodo de órbita')
        sys.exit()


    h = (G*M*T**2/(4*pi**2))**(1/3) - R
    print("La altura de la orbita desde la superficie de la tierra es {} m\n".format(h))


# Se concluye que no es posible que el satélite orbite la tierra cada 45 segundos ya que necesitaría orbitar a una distancia por debajo de la superficie de la tierra.

# \subsection*{d}

# Un día sideral es el tiempo que se tarda el planeta Tierra en completar una rotación sobre se propio eje, mientras que el día solar (el de 24 horas) es el tiempo que se tarda una persona en la Tierra observar que el sol llegue al mismo punto en el cielo.

# Si corremos el programa una vez más veremos que la diferencia es significativa

# In[130]:


t=["23.93h","24h" ]
H=[]
for i,T in enumerate(t):

    if "s" in T:
        T=float(T.strip("s"))

    elif "min" in T:
        T=float(T.strip("min"))
        T=T*minute

    elif "h" in T:
        T=float(T.strip("h"))
        T=T*hour
    else:
        print('ingrese unidades al periodo de órbita')
        sys.exit()


    h = (G*M*T**2/(4*pi**2))**(1/3) - R
    H.append(h)
    print("La altura de la orbita para un período de {} s es {} m\n".format(t[i],h))
diff=abs(H[0]-H[1])
print('La diferencia entre las alturas es de {} metros'.format(diff))
