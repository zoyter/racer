import random as rnd
import pygame as pyg
from pygame.locals import *

# Глобальные функции
def loadimg(fname):
    ''' Загрузчик картинок
        На вход подается имя файла с картинкой
    '''
    # Находим расширение файла: PNG или  JPEG
    ext = fname.split('.')[-1]
    if ext == 'png':
        # Если это PNG то загружаем картинку в память с сохранением прозрачности
        img = pyg.image.load(fname).convert_alpha()
        img = pyg.transform.scale(img,(74,150))
    else:
        # Если это JPEG, то просто грузим в память
        img = pyg.image.load(fname).convert()
    # Возвращаем загруженную картинку и
    # прямоугольник в который она вписана (т.е. ее размеры)
    return img, img.get_rect()

def rndcolor():
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    return (r, g, b)
