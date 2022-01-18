
import keyword
import pygame
import sys
import time
import random
import change_tuple
import movement
import pygame.freetype



class Display:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = 5
        self.max_x = 1000
        self.max_y = 500
        self.score = 0
        self.vector = 'd'
        self.width = 107
        self.height = 99


    def window(self):
        pygame.init()
        display = pygame.display.set_mode((self.max_x, self.max_y))
        player_texture= pygame.image.load("toast.png")
        pygame.display.set_caption("Game")
        fpsclock = pygame.time.Clock()
        draw_player = display.blit(player_texture, (self.x, self.y, 50, 50))
        apple_x = random.randrange(99, self.max_x-50)
        apple_y = random.randrange(99, self.max_y-50)
        font = pygame.font.Font('freesansbold.ttf', 32)
        running = True
        starting_position = (self.x, self.y)
        while running:
            fpsclock.tick(60)
            display.fill([0,0,0])
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or movement.Movement(self.max_y, draw_player, self.y, "y", self.width, self.height).control_y(self.vector)==False\
                            or movement.Movement(self.max_x, draw_player, self.x, "x", self.width, self.height).control_x(self.vector)==False:
                        print(f"you have achieved {self.score} score. ")
                        pygame.quit()
                        return

                elif keys:
                    if keys[pygame.K_w] and self.vector != 's':
                        if self.vector != 'w':
                            self.y = self.y - 1
                            self.x = self.x + 0
                        self.vector = 'w'
                        continue
                        #self.y -= self.step
                    if keys[pygame.K_s] and self.vector != 'w':
                        if self.vector != 's':
                            self.y = self.y +1
                            self.x = self.x + 0
                        self.vector = 's'
                        continue
                        #self.y += self.step
                    if keys[pygame.K_d] and self.vector != 'a':
                        if self.vector != 'd':
                            self.y = self.y + 0
                            self.x = self.x + 1
                        self.vector = 'd'
                        continue
                        #self.x += self.step
                    if keys[pygame.K_a] and self.vector != 'd':
                        if self.vector != 'a':
                            self.y = self.y + 0
                            self.x = self.x - 1
                        self.vector = 'a'
                        continue
                        #self.x -= self.step

            if self.vector == 'w':
                self.y = self.y - 1
                self.x = self.x + 0
            elif self.vector == 's':
                self.y = self.y + 1
                self.x = self.x + 0
            elif self.vector == 'd':
                self.y = self.y + 0
                self.x = self.x + 1
            elif self.vector == 'a':
                self.y = self.y + 0
                self.x = self.x - 1


            self.x = movement.Movement(self.max_x, draw_player, self.x, "x", self.width, self.height).move()
            self.y = movement.Movement(self.max_y, draw_player, self.y, "y", self.width, self.height).move()
            #draw_player = display.blit(player_texture, [self.x, self.y, 50, 50])
            draw_player = pygame.draw.rect(display, [255, 225, 0], pygame.Rect(self.x, self.y, self.width, self.height))
            print(f"{self.score}")

            # score code
            text = font.render(f'Score: {self.score}', True, [255, 0, 0])
            textRect = text.get_rect()
            display.blit(text, textRect)
            pygame.display.flip()
                # end of score code
                # start of spawn code
            apple = pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))
            if draw_player.colliderect(apple):
                self.score += 1
                if self.max_y > self.height and self.max_x > self.width:
                    self.height += 5
                    self.width += 5
                elif self.max_y <= self.height or self.max_x <= self.width:
                    print("Vyhral jsi")

                apple_x = random.randrange(107, self.max_x-50)
                apple_y = random.randrange(107, self.max_y-50)
                apple = pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))


            pygame.display.update()


Display(250, 250).window()