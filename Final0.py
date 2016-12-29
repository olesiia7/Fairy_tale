import pygame, os, sys
#from Game import *
#from Menu import *
from pygame.locals import *

pygame.init()

class Final0:
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


        class FailPrincessDeath:
            def __init__(self):
                self.main()

            # Создаем экран
            def display(self):
                self.screen = pygame.display.set_mode((600, 530))
                pygame.display.set_caption('Позорное поражение...')

            # Фоновое изображение + варианты меню
            def update_display(self):
                image = pygame.image.load('Data/mainmenu.jpg')
                self.screen.blit(image, (0, 0))
                self.screen.blit(pygame.image.load('Data/deathp.png'), (180, 90))
                BigFont = pygame.font.Font('Data/Allods.ttf', 43)
                c = (255, 255, 255)
                self.screen.blit(BigFont.render('ПОЗОР!!!', 0, (252, 124, 71)), (225, 37))
                SmallFront = pygame.font.Font('Data/Allods.ttf', 28)
                x = 50
                y = 360
                self.screen.blit(SmallFront.render('Ты, нены НЕ уважаемы рыцарь,', 0, c), (x+30, y))
                self.screen.blit(SmallFront.render('не только НЕ СПАС возлюбленную,', 0, c), (x-30 + 30, y + 30))
                self.screen.blit(SmallFront.render('а сам же ее своею рукой и погубил!', 0, c), (x - 10, y  + 60))

                # Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
                self.try_again.create_button(self.screen, (60, 142, 255), 50, 460, 500, 50, 0, 'Я воскрешу и спасу возлюбленную!',
                                           (255, 255, 255))
                pygame.display.flip()

            def main(self):
                self.try_again = Button()
                self.display()
                while True:
                    self.update_display()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == MOUSEBUTTONDOWN:
                            if self.try_again.pressed(pygame.mouse.get_pos()):
                                    #a = Game()

                                    sys.exit()

        FailPrincessDeath = FailPrincessDeath()