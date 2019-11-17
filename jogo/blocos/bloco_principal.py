import pygame
from constants import WIDTH, HEIGHT, HEIGHT_BLOCO, WIDTH_BLOCO
from bloco_pai import Bloco


class BlocoPrincipal(Bloco):
    def __init__(self, display, width=WIDTH, height=HEIGHT):
        x = (width / 2) - (WIDTH_BLOCO/2)
        y = height - HEIGHT_BLOCO
        super().__init__(display, x, y, width=width, height=height)

    def move(self, key=None):
        if key == pygame.K_LEFT:
            self._move_left()
        elif key == pygame.K_RIGHT:
            self._move_right()
            pass
        elif key == pygame.K_UP:
            pass
        elif key == pygame.K_DOWN:
            pass

        self.set_bloco()

    def set_bloco(self):
        self.display.blit(self.bloco, (self.x, self.y))

    def _move_left(self):
        if not self.x <= 0:
            self.x -= 20

    def _move_right(self):
        print(self.x)
        if not self.x >= WIDTH - WIDTH_BLOCO:
            self.x += 20
