from numpy import*
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
 
#Числовые данные для расчётов взяты из  публикации
Re=1.496*10**8
Te=365.24
Rm=2.28*10**8
Tm=689.98
ee=0.093
N=3600
Rs = 6.9551*10**5

def x(g):
         return Rm*(cos(g)-ee)
def y(g):
         return Rm*sqrt(1-ee**2)*sin(g)
def t(g):
         return Tm*(g-ee*sin(g))/2*pi
def X(g):
         return Re*cos(2*pi*t(g)/Te)
def Y(g):
         return Re*sin(2*pi*t(g)/Te)
     
#def xy(r,phi): 
#    return Rs*cos(phi), Rs*sin(phi)       

y = array([y(2*pi*i/N) for i in arange(0,N,1)])
x = array([x(2*pi*i/N) for i in arange(0,N,1)])
X = array([X(2*pi*i/N) for i in arange(0,N,1)])
Y = array([Y(2*pi*i/N) for i in arange(0,N,1)])
t = array([t(2*pi*i/N) for i in arange(0,N,1)])


Ac = (Rm+Re)/2*1.057
b = sqrt(Ac**2 - (Ac-Re)**2)
XX = linspace(Ac,-Ac)
YY = sqrt(b**2*(1 - XX**2/Ac**2))
LLL = XX-Ac+Re

fig = plt.figure()
plt.title("Гелиоцентрические орбиты  Земли и Марса")
plt.xlabel('x(g),X(g)')
plt.ylabel('y(g),Y(g)')

#phis=arange(0,2*pi,N) 
#plt.plot(xy(Rs,phis), c='y',ls='-')   
 
plt.plot(LLL,YY,label='Полет спутника')
plt.plot(x,y,label='Орбита Марса')
plt.plot(X,Y,label='Орбита Земли')
plt.legend()
plt.axes().set_aspect('equal')   
plt.show()