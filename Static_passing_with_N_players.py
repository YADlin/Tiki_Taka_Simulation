import numpy as np
import pygame
from pygame.locals import *
import sys
from math import e


def update(P_ball):
    BALL.update(P_ball)


def render(P, N):
    ground.fill(GREEN)
    render_statics(P, N)
    BALL.render()


def render_statics(P, N):
    for i in range(N):
        pygame.draw.circle(ground, WHITE, (P[0, i], P[1, i]), 10)


class Ball():

    def __init__(self, position, color, diameter):
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.dia = diameter

    def update(self, position):
        self.x = position[0]
        self.y = position[1]

    def render(self):
        pygame.draw.circle(ground, self.color,
                           (int(self.x), int(self.y)), self.dia)


w, h = 1305, 580
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

ground = pygame.display.set_mode((w, h))
ground.fill(GREEN)


running = True

N = 6

P1 = np.array([650, 100])
P2 = np.array([450, 200])
P3 = np.array([850, 200])
P4 = np.array([850, 380])
P5 = np.array([450, 380])
P6 = np.array([650, 480])

P = np.array([P1, P2, P3, P4, P5, P6])
P = np.transpose(P)

t = 0
m = 0.3
k = 0.2
dt = 0.01

# Initialising
P_ball = P[:, 0]

BALL = Ball(P_ball, BLACK, 5)

# Establishing the first passer and the receiver
P_passer = P[:, 0]
P_receiver = P[:, 4]


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    check = np.sum((P_ball == P_receiver)*1)
    if check == 2:
        t = 0
        i = np.shape(P_receiver)
        P_passer = P_receiver
        c = np.random.randint(0, N)
        P_receiver = P[:, c]

    t += dt

    l = P_receiver - P_passer
    V_ball = 1.2*(k/m)*l

    P_ball = (m/k)*(1 - e**(-k*t/m))*V_ball + P_passer

    if abs(np.linalg.norm(P_ball-P_receiver)) < 10:
        P_ball = P_receiver

    update(P_ball)
    render(P, N)

    pygame.display.update()
