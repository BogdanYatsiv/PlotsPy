# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from Polynomial import Polinom

#====PLOT====
t = np.linspace(0, 3, 51)# 51 dot betwen 0 and 3
y = t**2*np.exp(-t**2)

plt.plot(t,y)
plt.show()

#====BATTERFLY PLOT====
#x=sin(t)*(e^cos(t)-2cos(4t)+sin^5(1/12t))
#y=cos(t)*(e^cos(t)-2cos(4t)+sin^5(1/12t))
#t is[0;12π]

t = np.linspace(1, 12*np.pi,500)
x = np.sin(t)*(np.exp(np.cos(t)-2*np.cos(4*t)+np.sin(1/(12*t)**5)))
y = np.cos(t)*(np.exp(np.cos(t)-2*np.cos(4*t)+np.sin(1/(12*t)**5)))

plt.plot(x,y,"r--")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Batterfly")
#plt.legend()
plt.grid()
plt.show()

#====POLYNOMIAL PLOT====
dots = np.linspace(-10, 10, 30)
a = Polinom([(23,5),(13,1),(1,2)], 5)
b = Polinom([(-20,5),(13,3),(1,2),(5,7),(-10,10)], 10)
y_poly_a = a.count_plot(dots)
y_poly_b = b.count_plot(dots)
print(y_poly_a)
print(y_poly_b)

plt.xlabel("X")
plt.ylabel("Y")
plt.grid()

plt.plot(dots,y_poly_a)
plt.plot(dots,y_poly_b,"r--")
plt.show()