import random
import pygame


class Spawn_food:
    def __init__(self, display, draw_player):
        self.display = display
        self.height = display.get_height() - 99
        self.width = display.get_width() - 107
        self.player = draw_player
        self.spawn = True
        self.apple = 0


    def food(self):
        while self.spawn:
            if self.spawn:
                self.apple = pygame.draw.rect(self.display, [255, 0, 0], (random.randint(107, self.width), random.randint(99, self.height), 50, 50))
                self.spawn = False
                return False
        if pygame.Rect.colliderect(self.apple, self.player):
            self.spawn = True
            return True



