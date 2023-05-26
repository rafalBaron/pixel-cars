import pygame
from CONST import *


class Car(pygame.Rect):

    def __init__(self):
        self.height = 160
        self.width = 200
        self.x = int(SCREEN_SIZE[0]//2)
        self.y = int(SCREEN_SIZE[1]//2)

    def move(self):

        pass