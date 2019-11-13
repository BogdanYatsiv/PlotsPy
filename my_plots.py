# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from Polynomial import *

#====PLOT====
t = linspace(0, 3, 51)# 51 dot betwen 0 and 3
y = t**2*exp(-t**2)

plt.plot(t,y)
plt.show()

#====BATTERFLY PLOT====
#x=sin(t)*(e^cos(t)-2cos(4t)+sin^5(1/12t))
#y=cos(t)*(e^cos(t)-2cos(4t)+sin^5(1/12t))
#t is[0;12π]

t = linspace(0, 12*np.pi,500)
x = sin(t)*(exp(cos(t)-2*cos(4*t)+sin(1/(12*t)**5)))
y = cos(t)*(exp(cos(t)-2*cos(4*t)+sin(1/(12*t)**5)))

plt.plot(x,y,"r--")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Batterfly")
#plt.legend()
plt.grid()
plt.show()

#====LEMINISKATA BERNULI====
# theta = np.arange
dots = linspace(0, 10, 10)
cont = [(23,5),(13,1),(1,2)]
a = Polinom(cont,5)
poly_y = a(dots,2)

plt.plot(dots,poly_y)
plt.show()