import numpy as np
import pygame
from pygame.locals import *
import sys
from math import e


def update(b):
    BALL.update(b)


def render():
    ground.fill(GREEN)
    render_statics()
    BALL.render()


def render_statics():
    pygame.draw.circle(ground, WHITE, (A, 240), 10)
    pygame.draw.circle(ground, GRAY, (B, 240), 10)


class Ball():

    def __init__(self, position, color, diameter):
        self.x = position
        self.color = color
        self.dia = diameter

    def update(self, position):
        self.x = position

    def render(self):
        pygame.draw.circle(ground, self.color, (int(self.x), 240), self.dia)


def pass_velocity(l, m, k, t=500):
    return (k*l)/(m*(1-e**(-k*t/m)))


w, h = 1300, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)

ground = pygame.display.set_mode((w, h))
ground.fill(GREEN)


running = True

A = 100
B = 1250
l = abs(A - B)
b = 100

m = 0.3
k = 0.2
dt = 0.01
V_pass = pass_velocity(l, m, k)
BALL = Ball(b, BLACK, 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    n = 1 + 0.1*np.random.rand()
    if b == A:
        pygame.time.wait(1000)
        t = 0
        V = n*V_pass
        X = A
    elif b == B:
        pygame.time.wait(1000)
        t = 0
        V = -n*V_pass
        X = B
    t += dt
    A1 = -m*V/k
    A2 = X - A1
    b = A1*e**(-k*t/m) + A2

    # print(b,  t)

    if V > 0 and abs(b - B) < 10:
        b = B
    elif V < 0 and abs(b - A) < 10:
        b = A

    update(b)
    render()

    pygame.display.update()
