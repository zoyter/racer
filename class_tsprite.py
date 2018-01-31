import random as rnd
import pygame as pyg
from pygame.locals import *
from common import *

class TSprite(pyg.sprite.Sprite):
    def __init__(self, fname,x = 10,y = 10):
        super().__init__()
        # Загрузка картинки
        self.image, self.rect = loadimg(fname)
        # Цвет текста под спрайтом
        self.text_color = rndcolor()
        # Количество жизней
        self.life = 10
        # Высота строки графического интерфейса (т.е. наш спрайт должен быть ниже этого интерфейса)
        self.GUI_Height = 30
        # Задаем шрифт, которым будет выводится информация
        self.font = pyg.font.Font("data/font/Ru.ttf", 12)
        # получаем экран, на котором будет рисоваться спрайт
        self.screen = pyg.display.get_surface()
        # Сброс позиции вывода спрайта
        self.rnd_pos()

    def  rnd_pos(self):
        """ Случайная позиция спрайта
        """
        self.rect.x = rnd.randint(250, 480)
        self.rect.y = -1* rnd.randint(0,500)

    def print_life(self):
        # формируем текстовую строку с количеством жизней
        t = str(self.life)
        # генерируем картинку с текстом
        text = self.font.render(t,True,self.text_color)
        # позиционируем надпись под картинкой спрайта
        x = self.rect.x + self.rect.width //2 - text.get_width() //2
        y = self.rect.y + self.rect.height
        # отрисовываем текст
        self.screen.blit(text,[x,y])        

    def render(self):
        """ Отрисовка спрайта
        """
        x = self.rect.x
        y = self.rect.y
        self.screen.blit(self.image,[x,y])
        self.print_life()

    def update(self):
        """ Обновление состояния спрайта
            например, можно его тут подвигать и т.п.
        """
        r = 0
        self.rect.y += 5
        if self.rect.y > self.screen.get_height():
            self.rnd_pos()
            self.rect.y = 0 - self.rect.height
            #r = -1
        return r
