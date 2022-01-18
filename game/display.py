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
    def window(self):
        pygame.init()
        display = pygame.display.set_mode((self.max_x, self.max_y))
        player_texture = pygame.image.load("toast.png")
        pygame.display.set_caption("Game")
        fpsclock = pygame.time.Clock()
        draw_player = display.blit(player_texture, (self.x, self.y, 50, 50))
        apple_x = random.randrange(99, self.max_x-50)
        apple_y = random.randrange(99, self.max_y-50)
        #pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 5, 5))
        font = pygame.font.Font('freesansbold.ttf', 32)

        dir = (1, 0)
        while True:
            fpsclock.tick(60)
            display.fill([0,0,0])
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return


                elif keys:
                    if keys[pygame.K_w]:
                        self.y = self.y - 1
                        self.x = self.x + 0
                        self.vector = 'w'
                        #self.y -= self.step
                    if keys[pygame.K_s]:
                        self.y = self.y +1
                        self.x = self.x + 0
                        self.vector = 's'
                        #self.y += self.step
                    if keys[pygame.K_d]:
                        self.y = self.y + 0
                        self.x = self.x + 1
                        self.vector = 'd'
                        #self.x += self.step
                    if keys[pygame.K_a]:
                        self.y = self.y + 0
                        self.x = self.x -1
                        self.vector = 'a'
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

            self.x = movement.Movement(self.max_x, draw_player, self.x, "x").move()
            self.y = movement.Movement(self.max_y, draw_player, self.y, "y").move()
            #draw_player = display.blit(player_texture, (self.x, self.y, 50, 50))
            draw_player = display.blit(player_texture, (self.x, self.y, 50, 50))
            print(f"{self.score}")

            #score code
            text = font.render(f'Score: {self.score}', True, [255, 0, 0])
            textRect = text.get_rect()
            display.blit(text, textRect)
            pygame.display.flip()
                #end of score code

                #start of spawn code
            apple = pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))
            if draw_player.colliderect(apple):
                self.score += 1
                apple_x = random.randrange(107, self.max_x-50)
                apple_y = random.randrange(107, self.max_y-50)
                apple = pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))
            pygame.display.update()

# class spawn:
#     def __init__(self, max_x, max_y, score, display, player):
#         self.max_x = max_x
#         self.max_y = max_y
#         self.score = score
#         self.display = display
#         self.player = player
#     def food(self):
#         apple_x = random.randrange(107, self.max_x - 50)
#         apple_y = random.randrange(107, self.max_y - 50)
#         apple = pygame.draw.rect(self.display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))
#
#         if self.player.colliderect(apple):
#             self.score += 1
#             apple_x = random.randrange(107, self.max_x - 50)
#             apple_y = random.randrange(107, self.max_y - 50)
#             return pygame.draw.rect(self.display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))

Display(250, 250).window()