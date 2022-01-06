import keyword

import pygame
import sys
import time
import random
import change_tuple
import movement



class Display:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = 5
        self.max_x = 1000
        self.max_y = 500
    def window(self):
        pygame.init()
        display = pygame.display.set_mode((self.max_x, self.max_y))
        player_texture = pygame.image.load("toast.png")
        pygame.display.set_caption("Game")
        fpsclock = pygame.time.Clock()
        draw_player = display.blit(player_texture, (self.x, self.y, 50, 50))
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
                        self.y -= self.step
                    if keys[pygame.K_s]:
                        self.y += self.step
                    if keys[pygame.K_d]:
                        self.x += self.step
                    if keys[pygame.K_a]:
                        self.x -= self.step
                self.x = movement.Movement(self.max_x, draw_player, self.x, "x").move()
                self.y = movement.Movement(self.max_y, draw_player, self.y, "y").move()
                display.blit(player_texture, (self.x, self.y, 50, 50))

                pygame.display.flip()

                pygame.display.update()

# class Movement:
#     def __init__(self, display, player, xy):
#         self.display = display
#         self.player = player
#         self.x = xy
#
#     def control_x(self):
#         rec_color = [255, 0, 0]
#         rect_x = pygame.draw.rect(self.display, rec_color, pygame.Rect(0, 0, 5, self.display.get_height()))
#         rect_minusx = pygame.draw.rect(self.display, rec_color,
#                                        pygame.Rect(self.display.get_width() - 5, 0, 5, self.display.get_height()))
#         collide_x = self.player.colliderect(rect_x)
#         collide_minusx = self.player.colliderect(rect_minusx)
#         if collide_x:
#             self.x += 5
#             return self.x
#         elif collide_minusx:
#             self.x -= 5
#             return self.x
#         return self.x
#
#     def control_y(self):
#         re_color = [0, 255, 0]
#         rect_y = pygame.draw.rect(self.display, re_color, pygame.Rect(0, 0, self.display.get_width(), 5))
#         rect_minusy = pygame.draw.rect(self.display, re_color, pygame.Rect(0, self.display.get_height() - 5, self.display.get_width(), 5))
#         collide_y = self.player.colliderect(rect_y)
#         collide_minusy = self.player.colliderect(rect_minusy)
#         if collide_y:
#             self.x += 5
#             return self.x
#         elif collide_minusy:
#             self.x -= 5
#             return self.x
#         return self.x


Display(250, 250).window()