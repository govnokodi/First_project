import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
 
#Числовые данные для расчётов взяты из  публикации
REarthOrbit=1.496*10**8
Te=365.24
RMarsOrbit=2.28*10**8
Tm=689.98
ee=0.093
N=360
T = 100
DD = 1.057
Rs = 6.9551*10**5
REarth = 6.371*10**3
RMars = 3.3895*10**3

Ae = REarthOrbit

def x(g):
         return RMarsOrbit*(np.cos(g)-ee)
def y(g):
         return RMarsOrbit*np.sqrt(1-ee**2)*np.sin(g)
def t(g):
         return Tm*(g-ee*np.sin(g))/2*np.pi
def X(g):
         return REarthOrbit*np.cos(2*np.pi*t(g)/Te)
def Y(g):
         return REarthOrbit*np.sin(2*np.pi*t(g)/Te)
     
#def xy(r,phi): 
#    return Rs*cos(phi), Rs*sin(phi)       

y = np.array([y(2*np.pi*i/N) for i in np.arange(0,N,1)])
x = np.array([x(2*np.pi*i/N) for i in np.arange(0,N,1)])
X = np.array([X(2*np.pi*i/N) for i in np.arange(0,N,1)])
Y = np.array([Y(2*np.pi*i/N) for i in np.arange(0,N,1)])
t = np.array([t(2*np.pi*i/N) for i in np.arange(0,N,1)])

Ac = (RMarsOrbit+REarthOrbit)/2*DD
b = np.sqrt(Ac**2 - (Ac-REarthOrbit)**2)
XX = np.linspace(Ac,-Ac)
YY = np.sqrt(b**2*(1 - XX**2/Ac**2))
RealView = XX-Ac+REarthOrbit

fig = plt.figure()
plt.title("Гелиоцентрические орбиты  Земли и Марса")
plt.xlabel('Астрономические единицы')
plt.ylabel('Астрономические единицы')

#phis=arange(0,2*pi,N) 
#plt.plot(xy(Rs,phis), c='y',ls='-')   
   
plt.plot(RealView/Ae,YY/Ae,label='Полет спутника')
plt.plot(x/Ae,y/Ae,label='Орбита Марса')
plt.plot(X/Ae,Y/Ae,label='Орбита Земли')
plt.legend()
plt.axes().set_aspect('equal')   
plt.show()


#def MArsCircle(x, y, RMars, N):
#    xRMars = zeros(N)
#    yRMars = zeros(N)
#    for i in range (0, N, 1):
#        alpha = linspace(0, 2*pi, N)
#        xRMars = x + REarth*cos(alpha) 
#        yRMars = y + REarth*sin(alpha)
#    return xRMars,yRMars

#def EarthCircle(X, Y, REarth, N):
#    xREarth = zeros(N)
#    yREarth = zeros(N)
#    for i in range (0, N, 1):
#        alpha = linspace(0, 2*pi, N)
#        xREarth = X + REarth*cos(alpha) 
#        yREarth = Y + REarth*sin(alpha)
#    return xREarth,yREarth

anim_list = []
for i in range(0, T, 1):
#    xEarthCir, yEarthCir = EarthCircle(X[i],Y[i],REarth, N)
#    Earth, = plt.plot(xEarthCir, yEarthCir, 'r-', lw=2)
#    xMarsCir, yMarsCir = MArsCircle(x[i],y[i],REarth, N)
#    Mars, = plt.plot(xMarsCir, yMarsCir, 'g-', lw=2)
    Polet, = plt.plot(RealView/Ae,YY/Ae, 'b-', lw = 1)
    point, = plt.plot(RealView/Ae, YY/Ae, 'bo' , lw = 1)
    MARS, = plt.plot(x/Ae,y/Ae, 'r-', lw = 1)
    MARSpoint, = plt.plot(x/Ae,y/Ae, 'ro', lw = 1)
    EARTH, = plt.plot(X/Ae,Y/Ae, 'g-', lw = 1)
    EARTHpoint, = plt.plot(X/Ae,Y/Ae, 'go', lw = 1)
    
    anim_list.append([EARTH,EARTHpoint,MARS,MARSpoint,Polet,point])
    
    
plt.axes().set_aspect('equal')   
ani = ArtistAnimation(fig, anim_list, interval=100)
ani.save('ni4ego_ne_polu4aetsa.gif')
