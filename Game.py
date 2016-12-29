import pygame, os, sys
from Menu import *
from Final0 import *
from Final1 import *
from Final2 import *

class StartGame:
    def __init__(self):
        self.main()

    def main(self):
        window = pygame.display.set_mode((600, 530))
        pygame.display.set_caption('Рыцарь, спаси принцессу!')
        screen = pygame.Surface((600, 530))

        pygame.font.init()
        speed_font = pygame.font.Font('Data/Allods.ttf', 60)

        # функция для занпузки изображений
        def load_image(name):
            fullname = os.path.join('data', name)
            try:
                image = pygame.image.load(fullname)
            except pygame.error:  # Мало ли :)
                print('Не удалось загрузить изображение: ', name)
                raise SystemExit
            image = image.convert_alpha()
            return image, image.get_rect()

        # заливаем фон
        def draw_background():
            back, back_rect = load_image('polyana2.jpg')
            screen.blit(back, (0, 0))
            return back

        x = 0
        y = 0
        point = 0
        unpoint = 5

        # создаем класс героев
        class Sprite:
            def __init__(self, xpos, ypos, filename):
                self.x = xpos
                self.y = ypos
                self.bitmap = pygame.image.load(filename)

            def render(self):
                screen.blit(self.bitmap, (self.x, self.y))

        # герои
        hero = Sprite(66, 415, 'Data/hero2.png')
        dragon = Sprite(-20, 80, 'Data/dragonNo.png')
        dragon.go_right = True
        dragon.step = 2
        Princess = Sprite(290, 40, 'Data/Princess2.png')
        # оружие
        sword = Sprite(200, 200, 'Data/sword40.png')
        sword.push = False
        fire = Sprite(300, 200, 'Data/fire50.png')
        fire.push = False
        # Локации
        castle = Sprite(310, -5, 'Data/castle.png')
        home = Sprite(5, 400, 'Data/home.png')
        # Камни
        stone = Sprite(120, 310, 'Data/stone.png')
        stone1 = Sprite(350, 170, 'Data/stone.png')
        stone2 = Sprite(500, 350, 'Data/stone.png')
        # счётчики
        heropoint = Sprite(7, 5, 'Data/points.png')
        heart = Sprite(95, 4, 'Data/heart.png')

        # Пересечение (столкновение) объектов
        def Interdect(x1, i1, x2, i2, y1, y2, j1, j2):
            if (x1 > x2 - i1) and (x1 < x2 + i2) and (y1 > y2 - j1) and (y1 < y2 + j2):
                return 1
            else:
                return 0

        reason = 3
        # 0 - попал в Принцессу
        # 1 - Рыцаря убил Дракон
        # 2 - Победил Дракона - спас принцессу!

        # закрытие при нажатии "Х"
        done = True
        # pygame.key.set_repeat(1,1)
        while done:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    done = False

                    # Управлние героем
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    if (hero.x > -15) and (Interdect(hero.x, 0, stone.x, 43, hero.y, stone.y, 63, 35) == False) and (
                        Interdect(hero.x, 0, stone1.x, 43, hero.y, stone1.y, 63, 35) == False) and (
                        Interdect(hero.x, 0, stone2.x, 43, hero.y, stone2.y, 63, 35) == False):
                        hero.x -= 4
                if e.key == pygame.K_RIGHT:
                    if hero.x < 529 and (Interdect(hero.x, 45, stone.x, 0, hero.y, stone.y, 63, 35) == False) and (
                        Interdect(hero.x, 45, stone1.x, 0, hero.y, stone1.y, 63, 35) == False) and (
                        Interdect(hero.x, 45, stone2.x, 0, hero.y, stone2.y, 63, 35) == False):
                        hero.x += 4
                if e.key == pygame.K_DOWN:
                    if hero.y < 415 and (Interdect(hero.x, 45, stone.x, 43, hero.y, stone.y, 63, 0) == False) and (
                        Interdect(hero.x, 45, stone1.x, 43, hero.y, stone1.y, 63, 0) == False) and (
                        Interdect(hero.x, 45, stone2.x, 43, hero.y, stone2.y, 63, 0) == False):
                        hero.y += 4
                if e.key == pygame.K_UP:
                    if hero.y > 200 and (Interdect(hero.x, 45, stone.x, 43, hero.y, stone.y, 0, 35) == False) and (
                        Interdect(hero.x, 45, stone1.x, 43, hero.y, stone1.y, 0, 35) == False) and (
                        Interdect(hero.x, 45, stone2.x, 43, hero.y, stone2.y, 0, 35) == False):
                        hero.y -= 4
                # проверяем, выпущена ли стрела
                if e.key == pygame.K_SPACE:
                    if sword.push == False:
                        sword.x = hero.x + 42
                        sword.push = True
                # проверяем, выпущен ли огонь
                if (dragon.x > hero.x - 20) and (dragon.x < hero.x + 60):
                    if fire.push == False:
                        fire.x = dragon.x + 5
                        fire.y = dragon.y
                        fire.push = True

                        # Движение Дракона
            if dragon.go_right == True:
                dragon.x += dragon.step
                if dragon.x > 500:
                    dragon.go_right = False
            else:
                dragon.x -= dragon.step
                if dragon.x < -10:
                    dragon.go_right = True
                    # Движение стрелы
            if sword.y < 0:
                sword.push = False
            if sword.push == False:
                sword.x = hero.x + 42
                sword.y = hero.y
            else:
                sword.y -= 12
                # Меч попадает в Дракона
            if Interdect(sword.x, 40, dragon.x, 60, sword.y, dragon.y, 0, 40) == True:
                sword.push = False
                dragon.step += 0.4
                point += 1
                # Меч попадает в Камни
            if (Interdect(sword.x, 20, stone.x, 43, sword.y, stone.y, 0, 60) == True) or (
                Interdect(sword.x, 20, stone1.x, 43, sword.y, stone1.y, 0, 60) == True) or (
                Interdect(sword.x, 20, stone2.x, 43, sword.y, stone2.y, 0, 60) == True):
                sword.push = False
                # Меч попадает в принцессу
            if Interdect(sword.x, 10, Princess.x, 40, sword.y, Princess.y, 0, 60) == True:
                unpoint = -10
                reason = 0
                sword.push = False
                # Движение огня
            if fire.y > 530:
                fire.push = False
            if fire.push == False:
                fire.x = dragon.x + 5
                fire.y = dragon.y + 40
            else:
                fire.y += 12
                # Огонь попадает в героя
            if Interdect(fire.x, 20, hero.x, 60, fire.y, hero.y, 0, 20) == True:
                fire.push = False
                unpoint -= 1
                if unpoint == 0:
                    reason = 1
                # Огонь попадает в Камни
            if (Interdect(fire.x, 40, stone.x, 43, fire.y, stone.y, 53, 0) == True) or (
                Interdect(fire.x, 40, stone1.x, 63, fire.y, stone1.y, 53, 0) == True) or (
                Interdect(fire.x, 40, stone2.x, 43, fire.y, stone2.y, 53, 0) == True):
                fire.push = False

            if reason == 0:
                final = Final0()
            elif reason == 1:
                final = Final1()
            elif reason == 2:
                final = Final2()

                # Создание шрифтов
            pygame.font.init()
            speed_font = pygame.font.Font('Data/Allods.ttf', 60)

            # Отрисовка объектов
            screen.blit(speed_font.render(str(unpoint), 0, (252, 124, 71)), (165, 17))
            screen.blit(speed_font.render(str(point), 0, (252, 124, 71)), (72, 17))
            window.blit(screen, (0, 30))
            pygame.display.flip()
            bk = draw_background()
            home.render()
            castle.render()
            stone.render()
            stone1.render()
            stone2.render()
            hero.render()
            sword.render()
            Princess.render()
            dragon.render()
            fire.render()
            heropoint.render()
            heart.render()

#game = Game()
if __name__ == "__main__":
    a = MainMenu()




