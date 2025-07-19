from vpython import *
from math import pi, sin , cos
from numpy import arange,array,linspace


def rk4_2d(f,a,b,N,Init_cond=[0,0]):

    h = (b-a)/N

    tpoints = arange(a,b,h)
    xpoints = []
    ypoints = []

    r = array(Init_cond,float)

    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
    return tpoints,xpoints,ypoints



g =9.81
l =0.1 # 10cm = 0.1m
a=0
b=10
N=1000
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta =omega
    fomega =-(g/l)*sin(theta)
    return array([ftheta,fomega] ,float)

theta0=179*pi/180
omega=0
Init=[theta0,omega]
t,theta,omega=rk4_2d(f,a,b,N,Init_cond=Init)


x=l * cos(theta0 )
y=l * sin(theta0 )

rod = cylinder(pos=vector(0, 0, 0), axis=vector(x,y, 0), radius=l/30)
bob = sphere(pos=vector(x, y, 0), radius=l/10)
for theta in theta:
    rate(75)
    x=l * cos(theta - pi / 2)
    y=l * sin(theta - pi / 2)
    rod.axis = vector(x, y, 0)
    bob.pos = vector(x,y, 0)
