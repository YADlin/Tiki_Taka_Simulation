import numpy as np
from math import cos, sin, tan
import matplotlib.pyplot as plt


def angle(players, flag):
    theta = (players[1, 1] - players[0, 1]) / (players[1, 0] - players[0, 0])
    if flag == 1:
        return theta
    else:
        return -theta


players = np.array([[0.0, 0.0], [10.0, 10.0]])

# initial condition
ball = [players[0, :]]

# parameters
g = 9.81
mu = 0.65
V_pass = 15.0

time = np.arange(0.0, 20.0, 0.1)

th = angle(players, 1)
print(th)
xb_dot = V_pass*cos(th)
yb_dot = V_pass*sin(th)

C1 = xb_dot
C3 = yb_dot

C2 = players[0, 0]
C4 = players[0, 1]

Bx = []
By = []

for t in time:
    ball = [C2 + C1*t - ((mu*g*cos(th)*t**2)/2), C4 +
            C3*t - ((mu*g*sin(th)*t**2)/2)]
    Bx.append(ball[0])
    By.append(ball[1])

plt.plot(time, Bx)
plt.show()
