# -*- coding: utf-8 -*-
import pygame as pyg
import random as rnd
from pygame.locals import *
from class_twindow import *
from class_tsprite import *

def main():
    # Инициализация
    pyg.init()
    pyg.font.init()

    window = TWindow([800,600])
    window.load_image("data/img/bg01.jpg")
    window.sprites.append(TSprite("data/img/car_02.png"))
    window.sprites.append(TSprite("data/img/car_03.png"))

    # флаг того, что игра идет
    isGame = True
    # Основной цикл игры
    size = [800,600]
    while window.isGame:
        # Обрабатываем события клавиатуры
        for e in pyg.event.get():
            if e.type == QUIT:
                window.isGame = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    window.isGame = False
                if e.key == K_1:
                    window.toggle_fullscreen()
                if e.key == K_p:
                    if window.state == 0:
                        window.state = 2
                    elif window.state == 2:
                        window.state = 0
        
        window.clear()
        window.update()
        window.render()
        
        pyg.display.flip()
        window.clock.tick(60)


    pyg.quit()
    print("G A M E O V E R")
    quit()

if __name__ == "__main__":
    main()
