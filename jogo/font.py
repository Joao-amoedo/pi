from constants import BLACK, GREY
import pygame


class Font:
    def __init__(self, text='Score: '):
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def write(self, score):
        return self.font.render('{} {}'.format(self.text, score), True, BLACK,
                                GREY)
