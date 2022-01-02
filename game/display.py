import keyword

import pygame
import sys
import time
import random
import movement



class Display:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def window(self):
        pygame.init()
        display = pygame.display.set_mode((500, 400))
        player_texture = pygame.image.load("toast.png")
        pygame.display.set_caption("Game")
        texture = display.blit(player_texture, (self.x, self.y, 50, 50))

        fps = 30
        fpsclock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
            #difference = movement.Movement(self.x, self.y).move()
            texture = display.blit(player_texture, (self.x, self.y, 50, 50))
            pygame.display.flip()
            # window.fill(0)
            pygame.display.update()
            fpsclock.tick(fps)


Display(250,250).window()