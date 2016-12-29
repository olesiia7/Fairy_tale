import pygame, os, sys
from Game import *
from pygame.locals import *

pygame.init()

class MainMenu:
    def __init__(self):
        self.main()

    def main(self):
        class Button:
            def create_button(self, surface, color, x, y, length, height, width, text, text_color):
                surface = self.draw_button(surface, color, length, height, x, y, width)
                surface = self.write_text(surface, text, text_color, length, height, x, y)
                self.rect = pygame.Rect(x, y, length, height)
                return surface

            def write_text(self, surface, text, text_color, length, height, x, y):
                font_size = int(length // len(text))
                myFont = pygame.font.Font('Data/Allods.ttf', font_size)
                myText = myFont.render(text, 1, text_color)
                surface.blit(myText,
                             ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
                return surface

            def draw_button(self, surface, color, length, height, x, y, width):
                for i in range(1, 10):
                    s = pygame.Surface((length + (i * 2), height + (i * 2)))
                    s.fill(color)
                    alpha = (255 / (i + 2))
                    if alpha <= 0:
                        alpha = 1
                    s.set_alpha(alpha)
                    pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
                    surface.blit(s, (x - i, y - i))
                pygame.draw.rect(surface, color, (x, y, length, height), 0)
                pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)
                return surface

            def pressed(self, mouse):
                if mouse[0] > self.rect.topleft[0]:
                    if mouse[1] > self.rect.topleft[1]:
                        if mouse[0] < self.rect.bottomright[0]:
                            if mouse[1] < self.rect.bottomright[1]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False



        class Button_Game:
            def __init__(self):
                self.main()

            # Создаем экран
            def display(self):
                self.screen = pygame.display.set_mode((600, 530))
                pygame.display.set_caption('Выбор пути')

            # Фоновое изображение + варианты меню
            def update_display(self):
                image = pygame.image.load('Data/mainmenu.jpg')
                self.screen.blit(image, (0,0))
                self.screen.blit(pygame.image.load('Data/row.png'), (30, 5))
                BigFont = pygame.font.Font('Data/Allods.ttf', 43)
                c = (255,255,255)
                self.screen.blit(BigFont.render('А В ПОМОЩЬ ТЕБЕ', 0, (252, 124, 71)), (125, 37))
                SmallFront = pygame.font.Font('Data/Allods.ttf', 28)
                self.screen.blit(SmallFront.render('Советы мои да пожелания', 0, c), (115, 107))
                self.screen.blit(SmallFront.render('дракона сразить 10 раз', 0, c),(145, 132))
                self.screen.blit(SmallFront.render('да самому не пропасть.', 0, c), (135, 157))
                self.screen.blit(SmallFront.render('Да смотри принцессу свою', 0, c), (95, 202))
                self.screen.blit(SmallFront.render('возлюбленную береги от меча своего.', 0, c), (35, 227))
                self.screen.blit(SmallFront.render('Не дай дракону огнедышащему', 0, c), (90, 272))
                self.screen.blit(SmallFront.render('на глазах у возлюбленной', 0, c), (120, 297))
                self.screen.blit(SmallFront.render('сжечь 5 раз тебя', 0, c), (170, 322))
                self.screen.blit(SmallFront.render('потомкам на посмешище!', 0, c), (105, 347))

                # Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
                self.Button1.create_button(self.screen, (107, 142, 255), 140, 420, 300, 50, 0, 'Спасти принцессу!',
                                           (255, 255, 255))
                pygame.display.flip()

            def main(self):
                self.Button1 = Button()
                self.display()
                while True:
                    self.update_display()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == MOUSEBUTTONDOWN:
                            if self.Button1.pressed(pygame.mouse.get_pos()):
                                game = StartGame()
                                sys.exit()

        class Button_Next:
            def __init__(self):
                self.main()

            # Создаем экран
            def display(self):
                self.screen = pygame.display.set_mode((600, 530))
                pygame.display.set_caption('Выбор пути')

            # Фоновое изображение + варианты меню
            def update_display(self):
                image = pygame.image.load('Data/mainmenu.jpg')
                self.screen.blit(image, (0,0))
                self.screen.blit(pygame.image.load('Data/prediction.png'), (30,5))
                BigFont = pygame.font.Font('Data/Allods.ttf', 53)
                c = (255,255,255)
                self.screen.blit(BigFont.render('ПРЕДИСЛОВИЕ', 0, (252, 124, 71)), (145, 37))
                SmallFront = pygame.font.Font('Data/Allods.ttf', 28)
                self.screen.blit(SmallFront.render('Тебе предстоит играть за влюбленного', 0, c), (25, 107))
                self.screen.blit(SmallFront.render('рыцаря, которому отец принцессы', 0, c),(55, 132))
                self.screen.blit(SmallFront.render('дал от ворот поворот.', 0, c), (155, 157))
                self.screen.blit(SmallFront.render('Он запер её в каменном замке', 0, c), (65, 202))
                self.screen.blit(SmallFront.render('и посадил на стражу дракона.', 0, c), (65, 227))
                self.screen.blit(SmallFront.render('Лишь ты можешь помочь', 0, c), (100, 272))
                self.screen.blit(SmallFront.render('романтичному рыцарю', 0, c), (120, 297))
                self.screen.blit(SmallFront.render('разрушить все преграды на пути', 0, c), (50, 322))
                self.screen.blit(SmallFront.render('настоящей любви к прекрасной даме', 0, c), (25, 347))

                # Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
                self.Button1.create_button(self.screen, (107, 142, 255), 205, 420, 200, 50, 0, 'Продолжай!',
                                           (255, 255, 255))
                pygame.display.flip()

            # Run the loop
            def main(self):
                self.Button1 = Button()
                self.display()
                while True:
                    self.update_display()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == MOUSEBUTTONDOWN:
                            if self.Button1.pressed(pygame.mouse.get_pos()):
                                next = Button_Game()
        w = pygame.display.set_mode((10, 10))
        pygame.mixer.music.load('Data/sound.mp3')
        pygame.mixer.music.play()
        obj = Button_Next()
        while pygame.mixer.music.get_busy():
            pass


