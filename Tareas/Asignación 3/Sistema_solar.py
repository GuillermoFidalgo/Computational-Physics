from vpython import *
from math import cos,sin,pi
from numpy import arange,empty,log, array,append


# canvas(title='Solar system',
#      width=1200, height=800,center=vec(6e11,0,0))

c1=5.0e6
Radio=array([2440,6052,6371,3386,69173/9,57316/9],float)*c1
Radio=append(Radio,695500*1e5)

# print(Radio)

c2=2.09e9
Radio_orbita=array([57.9,108.9,149.6,227.9,778.5,1433.4,0],float)*c2
Periodo=[88,224.7,365.3,687.0, 4331.6, 10759.2,0.01]
Periodo=array(Periodo)


s= empty(len(Radio),sphere)
for i in arange(len(s)):
    s[i]=sphere(make_trail=True)
    
    
colores = [color.orange,color.red,color.blue,color.cyan,color.green,color.white,color.yellow]



# valores iniciales de cada esfera
for i in range(len(s)):
    s[i].color=colores[i]
    s[i].radius=Radio[i]
    s[i].pos=vec(Radio_orbita[i],0,0)
    



# Mover los planetas
    
# x=empty(len(s))    
# y=empty(len(s))    
omega=1/Periodo

for t in arange(0,1e5):
    for i in range(len(s)):
        rate(1000)
        x = Radio_orbita[i]*cos(omega[i]*t)
        y = Radio_orbita[i]*sin(omega[i]*t)
        s[i].pos = vec(x,y,0)
