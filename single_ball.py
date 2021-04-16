import numpy as np
import matplotlib.pyplot as plt
from math import e


K = 0.4
m = 0.5
x0 = 0.0
xdot0 = 1000.0
A1 = -xdot0*m/K
A2 = x0 - A1

t = np.arange(0.0, 10.0, 0.1)
x = A1*e**(-K*t/m) + A2
xdot = -(K/m)*A1*e**(-K*t/m)

plt.plot(t, x, label='position of ball')
plt.plot(t, xdot, label='velocity of ball')
plt.xlabel('time')
plt.legend()
plt.show()
