import numpy as np
import matplotlib.pyplot as plt

# Initial distance between the player and the ball (# Ball here is static for simplification)
L = 10

# Initial Velocity of the player
V_ini = 3

# The initial three zone velocity gradients
a_dec = -0.4*V_ini/L

# The acceleration in the other two zones
a_inc = 0.1
a_snatch = 0.3

Dist = np.array(np.arange(0, L))
Velo = np.zeros((L,))
Lx = 0

for i in range(L):
    if (i <= L/2):
        Velo[i] = V_ini*(1-(0.4*i/L))
        V1 = Velo[i]
    elif (i > L/2 and i < 0.9*L):
        Velo[i] = V1*0.2 + a_inc*i
        V2 = Velo[i]
    elif (i >= 0.9*L):
        Velo[i] = V2 + a_snatch*i

plt.plot(Dist, Velo)
plt.xlabel('Distance')
plt.ylabel('Velocity')
plt.show()
