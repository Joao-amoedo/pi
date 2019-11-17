import pygame
from constants import WIDTH, HEIGHT
from os.path import dirname

path_bloco_png = dirname(__file__) + '/bloco.png'


class Bloco:
    def __init__(self, display, x, y, width=WIDTH, height=HEIGHT):
        self.bloco = pygame.image.load(path_bloco_png)
        self.width = width
        self.height = height
        self.display = display
        self.x = x
        self.y = y
        self.set_bloco()

    def set_bloco(self):
        self.display.blit(self.bloco, (self.x, self.y))
    