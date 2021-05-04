import numpy as np
import pygame
from pygame.locals import *
import sys
from math import e

class Chaser():

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

