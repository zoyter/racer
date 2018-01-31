import random as rnd
import pygame as pyg
from pygame.locals import *
from common import *

class TRoad(pyg.sprite.Sprite):
    def __init__(self, fname,x = 10,y = 10):
        super().__init__()
        # Загрузка картинки
        self.image, self.rect = loadimg(fname)
        self.image = pyg.transform.scale(self.image,(10,100))
        self.rect.width = 10
        self.rect.height = 100
        # получаем экран, на котором будет рисоваться спрайт
        self.screen = pyg.display.get_surface()
        self.rect.x = self.screen.get_width() // 2 - self.rect.width // 2

    def render(self):
        """ Отрисовка спрайта
        """
        x = self.rect.x
        y = self.rect.y
        self.screen.blit(self.image,[x,y])

    def update(self):
        """ Обновление состояния спрайта
            например, можно его тут подвигать и т.п.
        """
        self.rect.y += 5
        if self.rect.y > self.screen.get_height():
            self.rect.y = -100
