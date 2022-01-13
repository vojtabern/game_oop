import keyword

import pygame
import sys
import time
import random
import change_tuple
import movement
import spawn
import pygame.freetype



class Display:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = 5
        self.max_x = 1000
        self.max_y = 500
        self.score = 0
    def window(self):
        pygame.init()
        display = pygame.display.set_mode((self.max_x, self.max_y))
        player_texture = pygame.image.load("toast.png")
        pygame.display.set_caption("Game")
        fpsclock = pygame.time.Clock()
        draw_player = display.blit(player_texture, (self.x, self.y, 50, 50))
        apple_x = random.randrange(99, display.get_width())
        apple_y = random.randrange(99, display.get_height())
        pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 5, 5))
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
                draw_player = display.blit(player_texture, (self.x, self.y, 50, 50))
                print (f"{self.score}")

                pygame.display.flip()
                apple = pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))
                if draw_player.colliderect(apple):
                    self.score += 1
                    apple_x = random.randrange(107, display.get_width())
                    apple_y = random.randrange(107, display.get_height())
                    apple = pygame.draw.rect(display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))
                pygame.display.update()


Display(250, 250).window()