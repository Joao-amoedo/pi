# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:59:23 2019

@author: jp-ad
"""

import pygame
from blocos import BlocoPrincipal, BlocoInimigo
from display import Display
from constants import WIDTH, HEIGHT, WIDTH_BLOCO, HEIGHT_BLOCO, GREY
from random import random, randint
from os.path import dirname
from sys import path
path.append(dirname(dirname(__file__)) + '/ia/rede_neural/')
from rede import Rede
from preprocessing import min_max_scaler


class Jogo:
    def __init__(self, qtd_inimigos=3, width=WIDTH, height=HEIGHT):
        pygame.init()
        self.display = Display(width=WIDTH, height=HEIGHT)
        self.clock = pygame.time.Clock()
        self.jogador = BlocoPrincipal(self.display, width=width, height=height)
        self.qtd_inimigos = qtd_inimigos
        self.enemys = []
        self.score = 0

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                self.jogador.move(event.key)
        return False

    def init(self, color_fill=GREY):
        fechou = False
        self._create_neural_network()
        while not fechou:
            self.display.fill(color_fill)
            self._create_enemy()
            self._enemys_fall()
            self._check_fall_enemy()
            fechou = self._check_colision() or fechou
            fechou = self._check_event() or fechou
            self.jogador.set_bloco()
            self.display.write_score(self.score)
            self._get_move_rna()
            self.display.update()
            self.clock.tick(60)

        pygame.quit()

    def _create_enemy(self, qtd=None, width=WIDTH, height=HEIGHT):

        qtd = qtd or self.qtd_inimigos

        while len(self.enemys) < qtd:
            x = randint(0, WIDTH - WIDTH_BLOCO)
            self.enemys.append(
                BlocoInimigo(x=x,
                             speed=random() * 10,
                             display=self.display,
                             width=width,
                             height=height))

    def _enemys_fall(self):
        [self.enemys[i].fall() for i in range(len(self.enemys))]

    def _check_fall_enemy(self):
        for idx, enemy in enumerate(self.enemys):
            if enemy.y >= (HEIGHT + HEIGHT_BLOCO):
                del self.enemys[idx]
                self.score += 1
                self._create_enemy()

    def _check_colision(self):
        for enemy in self.enemys:
            if enemy.y >= HEIGHT - HEIGHT_BLOCO:
                x = enemy.x
                x_high = x + (HEIGHT_BLOCO)
                x_low = x - (HEIGHT_BLOCO)
                if x_low <= self.jogador.x <= x_high:
                    return True
        return False

    def _create_neural_network(self, qtd_camadas=2):
        self.rede = Rede(1 + (self.qtd_inimigos * 3))
        [self.rede.add_camada(10) for i in range(qtd_camadas)]
        self.rede.add_camada(3)

    def _get_move_rna(self):
        inputs = self._get_inputs()
        print(inputs)
        predicts = self.rede.predict(inputs)
        max_predict = max(predicts)
        if max_predict == predicts[0]:
            self.jogador._move_left()
        if max_predict == predicts[1]:
            self.jogador._move_right()
        if max_predict == predicts[2]:
            pass

    def _get_inputs(self):
        inputs = []
        inputs += [min_max_scaler(0, WIDTH, enemy.x) for enemy in self.enemys]
        inputs += [min_max_scaler(0, HEIGHT, enemy.y) for enemy in self.enemys]
        inputs += [min_max_scaler(0, 10, enemy.speed) for enemy in self.enemys]
        inputs += [min_max_scaler(0, WIDTH, self.jogador.x)]
        return inputs
