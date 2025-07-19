#!/usr/bin/env python
# coding: utf-8

# ![](Final_a.png)

# \section*{a)}

# In[38]:


import numpy as np 
import matplotlib.pyplot as plt
omega0=3
gamma=.5
def f(r,t):

    x=r[0]
    dxdt=r[1]
    d2xdt2=-x*omega0**2 - gamma*dxdt
    return np.array([dxdt,d2xdt2],float)
    
def rk4_2d(f,a,b,N,Init_cond=[0,0]):
    h = (b-a)/N
    tpoints = np.arange(a,b,h)
    xpoints = []
    vpoints = []
    r = np.array(Init_cond,float)
    for t in tpoints:

        xpoints.append(r[0])
        vpoints.append(r[1])

        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    return tpoints,xpoints,vpoints


# In[39]:


a,b,N=0,20,10000
h = (b-a)/N
t,x,v=rk4_2d(f,a,b,N,Init_cond=[1,0])


# La solución para este tipo de ecuación diferencial tiene la forma siguiente
# $$ x= A_0 e^{-\gamma t/2 }\cos{\omega t}$$
# Verificamos si esto concuerda con nuestra solución numérica más abajo

# In[40]:


plt.figure(dpi=150)
plt.plot(t,x,label='Posición')
plt.plot(t,v,label='Velocidad')
plt.hlines(0,min(t),max(t),'k')
plt.ylabel('Posición\ny\n Velocidad',rotation=0,labelpad=30,size=12)
plt.xlabel('t',size=14)
plt.legend()
plt.title("Velocidad y Posición vs Tiempo",size=15)
plt.show()


# ![](Final_b.png)

# El perido se define como $$ T = \frac{2\pi}{\omega}$$ donde $\omega= \sqrt{\omega_0^2 - (\gamma/2)^2}$ y tenemos que $$T=\frac{2\pi}{\sqrt{\omega_0^2 - (\gamma/2)^2}}$$

# In[41]:


omega0=3
gamma=.5
omega=(omega0**2-(gamma/2)**2)**(.5)
T= 2*np.pi/omega
print("El periodo es",T,"s")
print("La frecuencia angular del sistema amortiguado es",omega,"Hz")


T= 2*np.pi/(omega0**2)**(.5)

print("\nSin amortiguamiento\nT = {} s\n".format(T))
for gamma in [1,2,3]:
#     if gamma==omega0:
#         print('El perido con gamma={} es infinito ya que hay amortiguamiento crítico'.format(gamma))
#         continue
    T= 2*np.pi/(omega0**2-(gamma/2)**2)**(.5)
    print('El perido con gamma={} es {} s'.format(gamma,T))


# ![](Final_b.png)

# Vemos que sin amortiguamiento el período es más corto y que mientras más amortiguamiento haya el periodo aumenta.
# Esto es porque la cantidad de oscilaciones por segundo se están disminuyendo hasta llegar a 0, lo que causa que $T =\dfrac{2\pi}{\omega}$ aumente.

# Con esta información verificamos si nuestra solución numérica corresponde a la analítica

# In[42]:


omega0=3
gamma=.5
omega=(omega0**2-(gamma/2)**2)**(.5)
T= 2*np.pi/omega

X=x[0]*np.exp(-gamma*t/2)*np.cos(omega*t)
plt.figure(dpi=150)
plt.plot(t,X,'r.')
plt.plot(t,x,'b--')
plt.title("Comparación entre soluciónes")
plt.ylabel("X",rotation=0)
plt.xlabel("T")
plt.legend(('Analítico',"Numérico"))
plt.show()


# Por lo visto no hay diferencias entre las soluciones 

# ![](Final_c.png)

# \section*{c) Computar el tiempo de relajamiento $\tau$}

# El tiempo $\tau$ tendrá la amplitud a un valor de $A_0/e\approx A_0 \times 0.37$

# Primero creamos una lista de las amplitudes en todo el movimiento

# In[43]:


A0=x[0] #Amplitud inicial
T0p5= 2*np.pi/omega # Periodo con gamma = 1/2
T=T0p5
Tplot=[0] # Inicializar lista de tiempos donde t = n*Periodo
A=[A0] #inicializar lista de Amplitudes máximas en todo el movimiento

# hallar los tiempos donde t es un múltiplo del período
for i,j in zip(t,x):
    if abs(i-T)<= h/2:
        A.append(j)
        Tplot.append(i)
        T+=T0p5
        


print("T ={}\n".format(Tplot))

print("A is",A)

Atau=np.array(A)*.37 # lista de amplitudes reducidas por .37

print("\nA_tau is {}\n".format(Atau))


# Hallar los tiempos tau en todo el movimiento 
tau=0
count=0
Tauplot=[] # lista de tiempos donde se reduce la amplitud
Tau=[] # lista del valor tau por cada ciclo (debe ser constante 1/gamma)
delta=1
for i,j in zip(x,t):
    if count==len(Atau) :
        break
    if (abs(i - Atau[count]) <= h/5) and i>0 and Tplot[count]<j and abs(Tplot[count]-j)>=delta:
        print("A es {:.3E}".format(Atau[count]))
        print("i es {:.3E}".format(i))
        print("t es {}".format(j))
        delta=j-tau
        Tau.append(delta)
        tau=j
        Tauplot.append(j)
        
        print("tau",delta)
        print("--"*10)
        count+=1


# In[74]:


#teórico
Aexp=A0*np.exp(-gamma*t/2)
count=0
tau=0
tau_teorico=[]
A_teor=[]
Tau_teo=[]
for Ax,j in zip(Aexp,t):
    if abs(Ax-Atau[count])<=h/20:
        print(Ax,"en tiempo",j)
        delta=j-tau
        tau_teorico.append(j)
        Tau_teo.append(delta)
        A_teor.append(Ax)
        count=count+1
        tau=j


# In[75]:


print(Tau_teo)


# In[72]:


# tao=[2*i/(gamma) for i in range(1,6)]
# print(tao)
# np.array(tao,float)

plt.figure(dpi=180)

plt.plot(t,x)
plt.plot(Tplot,A,'b.-')
plt.plot(Tauplot,Atau[:-1],'r.--')
# plt.plot(t,Aexp,',')
plt.plot(tau_teorico,A_teor,'.')

# plt.vlines(2/gamma,-1,1,"k")
# plt.hlines(Atau[:5],0,20,linewidth=1,colors='g')


# plt.plot(tao,Atau[:5],'.')
# plt.xticks(np.arange(0,21,1))
plt.grid()
plt.title(r"Amplitudes a tiempo $\tau$ para gamma = {}".format(gamma))
plt.legend(['x','amplitudes máximas',r'$\tau$ hallado',r'$\tau$ teórico'])
plt.show()


# Ahora repetimos para distintos valores de gamma

# In[33]:


A0=x[0] #Amplitud inicial
omega0=3
Gamma = np.array([1,2,3],float)
Omega=(omega0**2-(Gamma/2)**2)**(.5)
Periodos= 2*np.pi/Omega
print("Gamma=",Gamma)
print("Omega=",Omega)
print("Periodos =",Periodos)


# In[31]:


for T,gamma in zip(Periodos,Gamma):
    t,x,v=rk4_2d(f,a,b,N,Init_cond=[1,0])
    
    Tplot=[0] # Inicializar lista de tiempos donde t = n*Periodo
    A=[x[0]] #inicializar lista de Amplitudes máximas en todo el movimiento
    tempT=T
    # hallar los tiempos donde t es un múltiplo del período
    for i,j in zip(t,x):
        if abs(i-T)<= h/2:
            A.append(j)
            Tplot.append(i)
            tempT=tempT + T



    print("T ={}\n".format(Tplot))

    print("A is",A)

    Atau=np.array(A)*.37 # lista de amplitudes reducidas por .37

    print("\nA_tau is {}\n".format(Atau))


    # Hallar los tiempos tau en todo el movimiento 
    tau=0
    count=0
    Tauplot=[] # lista de tiempos donde se reduce la amplitud
    Tau=[] # lista del valor tau por cada ciclo (debe ser constante 1/gamma)
    delta=0

    for i,j in zip(x,t):
        if count==len(Atau) :
            break
        if (abs(i - Atau[count]) <= 1.4*h) and i>0  and abs(Tplot[count]-j)>=delta/2:
            print("A es {:.3E}".format(Atau[count]))
            print("i es {:.3E}".format(i))
            print("t es {}".format(j))
            
            delta=j-tau
            Tau.append(delta) 
            tau=j
            Tauplot.append(j)

            print("tau",delta)
            print("--"*10)
            count+=1
               
    print("---"*20)
#     plt.figure(dpi=180)
    print("gammas is {} and Tau is {}".format(gamma,Tau))
plt.plot(Gamma,Tau)
#     plt.plot(t,x)
#     plt.plot(Tplot,A,'b.-')
#     plt.plot(Tauplot,Atau,'r.--')
#     plt.grid()
#     plt.title(r"Amplitudes a tiempo $\tau$ para gamma = {}".format(gamma))
#     plt.legend(['x','amplitudes máximas',r'$\tau$ hallado'])
plt.show()


# $\tau$ disminuye con $\gamma$ de manera que $\tau \propto \frac1\gamma$

# ![](Final_d.png)

# La energía total es $E = T+U$ donde $ T = \frac12 mv^2$ y $ U= \frac12 kx^2$
# Si la ecuación diferencial es de la forma $$ \ddot{x} + \gamma \dot x +\omega_0^2x =0  $$  $ \gamma$ y $\omega_0$ pueden ser reescritas como $$ \gamma = \frac bm \qquad \omega_0^2 = \frac km $$
# Si tomamos que $m=1$ podemos calcular k necesaria para la energía potencial.
# Esta sería 

# In[96]:


k= omega0**2
Gamma = [1,2,3]
# print("k =",k)
plt.figure(dpi=150)
for gamma in Gamma:
    t,x,v=rk4_2d(f,a,b,N,Init_cond=[1,0])
    Tcinetica=.5*(1*np.array(v,float)**2)
    Upotencial= .5*(k*np.array(x,float))**2
#     print("T={}\nU={}".format(Tcinetica,Upotencial))
    E = Tcinetica+Upotencial
#     print("E=",E)
    plt.plot(t,E,label="Energía Total con $\gamma = {}$".format(gamma));
plt.legend()
plt.ylabel('E',rotation=0,labelpad=10)
plt.title("Energía total vs tiempo")
plt.xlabel('t')
plt.show()


# ![](Final_e.png)

# In[104]:


A0=x[0] #Amplitud inicial
omega0=3
Gamma = np.array([4,5,6,7,8],float)

Omega=(omega0**2-(Gamma/2)**2)**(.5) 
Periodos= 2*np.pi/Omega
print(Gamma)
print(Omega)
print(Periodos)
plt.figure(dpi=150)
for gamma in Gamma:
    
    t,x,v=rk4_2d(f,a,5,N,Init_cond=[1,0])
    plt.plot(t,x,label='x para $\gamma$ ={}'.format(gamma))
    plt.plot(t,v,label='v para $\gamma$ ={}'.format(gamma))
    plt.legend(bbox_to_anchor=(1.12,.5),loc=10,fontsize=7)
plt.title("Movimiento para $\gamma$={}".format(Gamma))
plt.ylabel('Velocidad y Posición')
plt.xlabel('Tiempo')
plt.show()


# El movimiento deja de ser oscilatorio para esto valores de $\gamma$ ya que el sistema se encuentra sobre amortiguado. El decaimiento es exponencial.

# ![](Final_f.png)

# In[108]:


A0=x[0] #Amplitud inicial
omega0=3
Gamma = np.array([.5,2,4,6,8],float)
Omega=(omega0**2-(Gamma/2)**2)**(.5)
Periodos= 2*np.pi/Omega
print(Gamma)
print(Omega)
print(Periodos)
plt.figure(dpi=150)
for gamma in Gamma:
    
    t,x,v=rk4_2d(f,a,b,N,Init_cond=[1,0])
    plt.plot(x,v,label=' para $\gamma$ ={}'.format(gamma))
    plt.legend(ncol=1,bbox_to_anchor=(1.15,.5),loc=10,fontsize=9)
plt.title("Diagrama de fase para $\gamma$={}".format(Gamma))
plt.ylabel("v",rotation=0,labelpad=10)
plt.xlabel('x')
plt.show()


# La trayectoria converge a $x=0$ y $v=0$ porque este es el estado al cual el sistema llega debido al amortiguamiento. Para toda $\gamma>0$ el diagrama de fase convergerá a este punto evenvtualmente.
