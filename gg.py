from numpy import*
import matplotlib.pyplot as plt

Re=1.496*10**8
Te=365.24
Rm=2.28*10**8
Tm=689.98
ee=0.093
N=360 

def polet (XX,YY,Ac,b):
    Ac = (Rm+Re)/2
    q = Re
    b = (Ac**2 - (Ac-q)**2)**1/2
    XX**2/Ac**2 + YY**2/b**2 = 1 
    
    