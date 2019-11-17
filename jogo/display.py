from constants import (WIDTH, HEIGHT, WHITE, GREY)
from pygame import display
from font import Font


class Display:
    def __init__(self, width=WIDTH, height=HEIGHT, title='A bit Racey'):
        self.game_display = display.set_mode((width, height))
        self.game_display.fill(GREY)
        self.font = Font()
        display.set_caption(title)

    def fill(self, color=GREY):
        self.game_display.fill(color)

    def update(self):
        display.update()

    def blit(self, object, x_y: tuple):
        self.game_display.blit(object, x_y)

    def write_score(self, score):
        text = self.font.write(score)
        self.blit(text, (WIDTH - 200, 50))
