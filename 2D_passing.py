import numpy as np

import pygame
from pygame.locals import *
import sys
from math import e


def update(P_ball):
    BALL.update(P_ball)


def render():
    ground.fill(GREEN)
    render_statics()
    BALL.render()


def render_statics():
    pygame.draw.circle(ground, WHITE, (A[0], A[1]), 10)
    pygame.draw.circle(ground, WHITE, (B[0], B[1]), 10)
    pygame.draw.circle(ground, WHITE, (C[0], C[1]), 10)


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


w, h = 1300, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

ground = pygame.display.set_mode((w, h))
ground.fill(GREEN)


running = True

A = np.array([100, 240])
B = np.array([500, 300])
C = np.array([575, 100])

m = 0.3
k = 0.2
dt = 0.01

# Initialising
P_ball = A

BALL = Ball(P_ball, BLACK, 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    P_Aball = np.sum((P_ball == A)*1)
    P_Bball = np.sum((P_ball == B)*1)
    P_Cball = np.sum((P_ball == C)*1)

    if P_Aball == 2:
        # pygame.time.wait(1000)
        t = 0
        P_passer = A
        c = np.random.randint(0, 2)
        P_receiver = (c*B) + (int(not(c))*C)

    elif P_Bball == 2:
        # pygame.time.wait(1000)
        t = 0
        P_passer = B
        c = np.random.randint(0, 2)
        P_receiver = (c*A) + (int(not(c))*C)

    elif P_Cball == 2:
        # pygame.time.wait(1000)
        t = 0
        P_passer = C
        c = np.random.randint(0, 2)
        P_receiver = (c*A) + (int(not(c))*B)
    t += dt

    l = P_receiver - P_passer
    V_ball = 1.2*(k/m)*l

    P_ball = (m/k)*(1 - e**(-k*t/m))*V_ball + P_passer

    if abs(np.linalg.norm(P_ball-P_receiver)) < 10:
        P_ball = P_receiver

    update(P_ball)
    render()

    pygame.display.update()
