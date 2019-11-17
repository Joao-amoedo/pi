from constants import WIDTH, HEIGHT, HEIGHT_BLOCO, WIDTH_BLOCO
from random import randint
from bloco_pai import Bloco


class BlocoInimigo(Bloco):
    def __init__(self, display, speed = 1, x=None, width=WIDTH, height=HEIGHT):
        xcor = randint(0, WIDTH - WIDTH_BLOCO) or x
        ycor = 0 - HEIGHT_BLOCO
        self.speed = speed
        super().__init__(display=display,
                         x=xcor,
                         y=ycor,
                         width=width,
                         height=height)

    def fall(self):
        self.y += self.speed
        self.set_bloco()
