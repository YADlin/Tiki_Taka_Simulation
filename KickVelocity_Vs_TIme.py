import matplotlib.pyplot as plt
import numpy as np
from math import e


m = 0.3
k = 0.2
l = 300
t = np.arange(0.1, 400, 0.1)
x_d = (k*l)/(m*(1-e**(-k*t/m)))

print(np.min(x_d))
plt.plot(t, x_d)

plt.show()
