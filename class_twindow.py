import random as rnd
import pygame as pyg
from pygame.locals import *
from common import *
from class_road import *

class TWindow():
    def __init__(self,size):
        """ Конструктор класса
            вход: ссылка на сам класс и размеры окна
        """
        # Инициализация дисплея
        pyg.display.init()
        # Задаем размер окна
        self.size = size
        # Получаем информацию о дисплее
        display_info = pyg.display.Info()
        # Находим текущие размеры экрана
        self.screen_size = [display_info.current_w, display_info.current_h]
        # Создаем окно заданного размера
        self.screen = pyg.display.set_mode(size)
        # Опускаем флаг состояния окна, т.е. сейчас находимся в оконном режиме
        self.window_state = False
        # Таймер
        self.clock = pyg.time.Clock()
        #Переменная для хранения фоновой картинки
        self.image = None
        #
        self.bgcolor = rndcolor()
        # Высота полоски в верхней части экрана
        self.GUI_Height = 30
        # Задаем шрифт, которым будет выводится информация
        self.font = pyg.font.Font("data/font/Ru.ttf", 16)        
        # Цвет текста 
        self.text_color = (255,255,255)

        # Задаем шрифт паузы
        self.font_menu = pyg.font.Font("data/font/Ru.ttf", 30)        
        # Цвет текста 
        self.menu_color = (255,0,0)

                
        # уровень
        self.level = 1
        # жизни
        self.life = 10
        # очки
        self.score = 0
        # Спрайты
        self.sprites = []
        # Флаг игры, если True, то игра идет, в противном случае игра завершена
        self.isGame = True
        # Состояние игры
        # 0 - обычная игра, 1 - меню, 2 - пауза, 3 - gameover
        self.state = 0

        self.lines = []
        self.lines.append(TRoad("data/img/line.png"))
        self.lines[0].rect.y = 0
        self.lines.append(TRoad("data/img/line.png"))
        self.lines[1].rect.y = self.screen.get_height() // 2 - self.lines[1].image.get_height() // 2
        self.lines.append(TRoad("data/img/line.png"))
        self.lines[2].rect.y = self.screen.get_height() - self.lines[1].image.get_height()
#        self.lines.append(TRoad("data/img/line.png"))
#        self.lines[3].rect.y = 600
        
    def toggle_fullscreen(self):
        """ Переключение между полноэкранным и оконным режимами
        """
        if self.window_state == False:
            print("Полноэкранный")
            pyg.display.set_mode(self.size, FULLSCREEN)
            self.window_state = not(self.window_state)
        else:
            print("Оконный")
            pyg.display.set_mode(self.size)
            self.window_state = not(self.window_state)

    def clear(self):
        """ Закрашиваем фон цветом или картинкой
        """
        if self.image == None:
            self.screen.fill(self.bgcolor)
        else:
            self.screen.blit(self.image,[0,0])

    def load_image(self, fname):
        """ Загрузка фоновой картинки
            Вход: ссылка на объект и путь к файлу
        """
        # Загружаем картинку
        self.image, self.rect = loadimg(fname)
        # Масштабируем картинку под размеры окна
        self.image = pyg.transform.scale(self.image,(self.screen.get_width(), self.screen.get_height()))

    def render_gui(self):        
        pyg.draw.rect(self.screen,(255,0,0),(0,0,self.screen.get_width(),self.GUI_Height),0)
        # формируем текстовую строку с количеством жизней
        t = "life: "+str(self.life)
        # генерируем картинку с текстом
        text = self.font.render(t,True,self.text_color)
        # позиционируем надпись под картинкой спрайта
        x = 10
        y = 2
        # отрисовываем текст
        self.screen.blit(text,[x,y])

        # формируем текстовую строку с количеством очков
        t = "score: "+str(self.score)
        # генерируем картинку с текстом
        text = self.font.render(t,True,self.text_color)
        # позиционируем надпись под картинкой спрайта
        x = self.screen.get_width() - text.get_width() - 10
        y = 2
        # отрисовываем текст
        self.screen.blit(text,[x,y])

        # формируем текстовую строку с текущим уровнем
        t = "level: "+str(self.level)
        # генерируем картинку с текстом
        text = self.font.render(t,True,self.text_color)
        # позиционируем надпись под картинкой спрайта
        x = self.screen.get_width() //2 - text.get_width() //2
        y = 2
        # отрисовываем текст
        self.screen.blit(text,[x,y])

    def render_pause(self):        
        # формируем текстовую строку с количеством жизней
        t = "P A U S E"
        # генерируем картинку с текстом
        text = self.font_menu.render(t,True,self.menu_color)
        # позиционируем надпись под картинкой спрайта
        x = self.screen.get_width() // 2 - text.get_width() // 2
        y = self.screen.get_height() // 2
        # отрисовываем текст
        self.screen.blit(text,[x,y])

    def render_gameover(self):        
        # формируем текстовую строку с количеством жизней
        t = "G A M E    O V E R"
        # генерируем картинку с текстом
        text = self.font_menu.render(t,True,self.menu_color)
        # позиционируем надпись под картинкой спрайта
        x = self.screen.get_width() // 2 - text.get_width() // 2
        y = self.screen.get_height() // 2
        # отрисовываем текст
        self.screen.blit(text,[x,y])

    def update(self):
        """ Обновление состояния спрайтов, начисление очков и штрафов, определение окончания игры
        """
        # Если игра находится в 0-м состоянии, то
        if self.state == 0:
            # Обновляем полоски на дороге
            for i in self.lines:
                i.update()
            # Обновляем спрайты
            for i in self.sprites:                
                r = i.update()
                # Если после обновления спрайта, оказалось, что курсор на нем, то
                if r > 0:
                    # мы попали по спрайту и заработали баллы
                    self.score += 1

                    # Дальше можно написать код, который будбет увеличивать уровень
                    # и менять картинку фона

                    
                elif r<0:
                    # если же спрайт улетел, то у нас отнимают очки здоровья
                    self.life -= 1
            if self.life <=0:
                self.state = 3
            
    def render(self):
        # Если состояние игра 0, то обновляем спрайты
        if self.state == 0:
            for i in self.lines:
                i.render()
            for i in self.sprites:
                i.render()
        # Если же состояние 2, то пауза
        elif self.state == 2:
            self.render_pause()
        # Если же состояние 3, то игра окончена
        elif self.state == 3:
            self.render_gameover()                   

        self.render_gui()
