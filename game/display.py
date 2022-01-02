import keyword

import pygame
import sys
import time
import random
import movement
import change_tuple



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
                xy = change_tuple.Vector2(self.x, self.y)
                max_xy = change_tuple.Vector2(self.max_x, self.max_y)
                position = movement.Movement(xy, max_xy).move()
                print(position)
                display.blit(player_texture, (position[0], position[1], 5, 5))

                pygame.display.flip()

                pygame.display.update()


Display(250, 250).window()