import numpy as np
import matplotlib.pyplot as plt

Re=1.496*10**8
Te=365.24
Rm=2.28*10**8
Tm=689.98
ee=0.093
N=360 

Ac = (Rm+Re)/2
q = Re
b = (Ac**2 - (Ac-q)**2)**(1/2)
XX = np.linspace(Rm+Re, N)
YY = (b**2*(1 - XX**2/Ac**2))**(1/2)
plt.axes().set_aspect('equal')
plt.plot(XX,YY, 'b-', lw=2)
plt.show()
