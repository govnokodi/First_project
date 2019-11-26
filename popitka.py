from numpy import*
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

fig = plt.figure()

#Числовые данные для расчётов взяты из  публикации
Re=1.496*10**8
Te=365.24
Rm=2.28*10**8
Tm=689.98
ee=0.093
N=360 

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
     

    
y=array([y(2*pi*i/N) for i in arange(0,N,1)])
x=array([x(2*pi*i/N) for i in arange(0,N,1)])
X=array([X(2*pi*i/N) for i in arange(0,N,1)])
Y=array([Y(2*pi*i/N) for i in arange(0,N,1)])
t=array([t(2*pi*i/N) for i in arange(0,N,1)])

Ac = (Rm+Re)/2
q = Re
b = (Ac**2 - (Ac-q)**2)**(1/2)
XX = np.linspace(-Rm,Rm,N)
YY = (b**2*(1 - XX**2/Ac**2))**(1/2)
    
figure()
title("Гелиоцентрические орбиты  Земли и Марса")
xlabel('x(g),X(g)')
ylabel('y(g),Y(g)')
plot(XX,YY,label='Полет спутника')
plot(x,y,label='Орбита Марса')
plot(X,Y,label='Орбита Земли')
plt.axes().set_aspect('equal')
    
show()

