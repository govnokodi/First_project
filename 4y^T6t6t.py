from numpy import*
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
 
#Числовые данные для расчётов взяты из  публикации
REarthOrbit=1.496*10**8
Te=365.24
RMarsOrbit=2.28*10**8
Tm=689.98
ee=0.093
N=3600
DD = 1.057
Rs = 6.9551*10**5
REarth = 6.371*10**3
RMars = 3.3895*10**3

Ae = REarthOrbit

def x(g):
         return RMarsOrbit*(cos(g)-ee)
def y(g):
         return RMarsOrbit*sqrt(1-ee**2)*sin(g)
def t(g):
         return Tm*(g-ee*sin(g))/2*pi
def X(g):
         return REarthOrbit*cos(2*pi*t(g)/Te)
def Y(g):
         return REarthOrbit*sin(2*pi*t(g)/Te)
     
#def xy(r,phi): 
#    return Rs*cos(phi), Rs*sin(phi)       

y = array([y(2*pi*i/N) for i in arange(0,N,1)])
x = array([x(2*pi*i/N) for i in arange(0,N,1)])
X = array([X(2*pi*i/N) for i in arange(0,N,1)])
Y = array([Y(2*pi*i/N) for i in arange(0,N,1)])
t = array([t(2*pi*i/N) for i in arange(0,N,1)])

Ac = (RMarsOrbit+REarthOrbit)/2*DD
b = sqrt(Ac**2 - (Ac-REarthOrbit)**2)
XX = linspace(Ac,-Ac)
YY = sqrt(b**2*(1 - XX**2/Ac**2))
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

def MArsCircle(x, y, RMars, N):
    xRMars = zeros(N)
    yRMars = zeros(N)
    for i in range (0, N, 1):
        alpha = linspace(0, 2*pi, N)
        xRMars = x + REarth*cos(alpha) 
        yRMars = y + REarth*sin(alpha)
    return xRMars,yRMars

def EarthCircle(X, Y, REarth, N):
    xREarth = zeros(N)
    yREarth = zeros(N)
    for i in range (0, N, 1):
        alpha = linspace(0, 2*pi, N)
        xREarth = X + REarth*cos(alpha) 
        yREarth = Y + REarth*sin(alpha)
    return xREarth,yREarth

anim_list = []
for i in range(0, N, 1):
    xEarthCir, yEarthCir = EarthCircle(X[i],Y[i],REarth, N)
    Earth, = plt.plot(xEarthCir, yEarthCir, 'r-', lw=2)
    
    xMarsCir, yMarsCir = MArsCircle(x[i],y[i],REarth, N)
    Mars, = plt.plot(xMarsCir, yMarsCir, 'g-', lw=2)
    
    liniaq, = plt.plot(RealView,YY, 'R-', lw=2)
    
    anim_list.append([liniaq,Earth,Mars])
