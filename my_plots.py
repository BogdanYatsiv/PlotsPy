# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from Polynomial import Polinom
from math import sqrt

#====PLOT====
t = np.linspace(0, 3, 51)# 51 dot betwen 0 and 3
y = t**2*np.exp(-t**2)

plt.plot(t,y,label = r"$t^2 * \exp(-t^2)$")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple plot")
plt.legend()
plt.grid()
plt.show()

#====BATTERFLY PLOT====
t = np.linspace(1, 12*np.pi,500)
x = np.sin(t)*(np.exp(np.cos(t)-2*np.cos(4*t)+np.sin(1/(12*t)**5)))
y = np.cos(t)*(np.exp(np.cos(t)-2*np.cos(4*t)+np.sin(1/(12*t)**5)))

plt.plot(x,y,"r--",label = r"""x = sin(t)*(exp(cos(t)-2*cos(4*t)+sin(1/(12*t)^5)))
y = cos(t)*(exp(cos(t)-2*cos(4*t)+sin(1/(12*t)^5)))""")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Batterfly plot")
plt.legend()
plt.grid()
plt.show()

#====POLYNOMIAL PLOT====
dots = np.linspace(-2, 2, 50)
a = Polinom([(23,5),(13,1),(1,2)], 5)
b = Polinom([(-20,5),(13,3),(1,2),(5,7),(-10,10)], 10)
y_poly_a = a(dots)
y_poly_b = b(dots)

print(y_poly_a)
print(y_poly_b)

plt.plot(dots,y_poly_a,label = str(a))
plt.plot(dots,y_poly_b,"r--",label = str(b))

plt.title("Polynomial plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()

#====LEMNISCATE OF BERNOULLI====
theta = np.arange(0, 2, 1/180)*np.pi

c = 10
plt.polar(theta, np.sqrt((2*c**2)*np.cos(2*theta)), label = r"$\sqrt{2c^2 * \cos(2\mu)}$")
plt.legend()
plt.show()