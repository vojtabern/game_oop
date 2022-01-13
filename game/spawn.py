import random
import pygame


class Spawn_food:
    def __init__(self, display, draw_player, snake_x, snake_y, apple_x, apple_y):
        self.display = display
        self.height = display.get_height() - 99
        self.width = display.get_width() - 107
        self.player = draw_player
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.apple_x = apple_x
        self.apple_y = apple_y


    def draw(self):
        # if not self.spawn:
        #     apple = pygame.draw.rect(self.display, [255, 0, 0],
        #                  (random.randint(107, self.width), random.randint(99, self.height), 50, 50))
        #     self.spawn = True
        # if pygame.Rect.colliderect(apple, self.player):
        #     self.spawn = False
        if self.snake_x == self.apple_x and self.snake_y == self.apple_y:
            #pygame.mixer.Sound.play(eat_apple_sound)
            #snakelength += 1
            self.apple_x = random.randrange(0, self.width)
            self.apple_y = random.randrange(0, self.height)
            new_apple = pygame.draw.rect(self.display, [255,0,0], pygame.Rect(self.apple_x, self.apple_y, 5, 5))
            return new_apple



