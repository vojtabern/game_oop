import random
import pygame


class Spawn_food:
    def __init__(self, display):
        self.display = display
        self.height = display.get_height() - 99
        self.width = display.get_width() - 107
        self.spawn = False
    def food(self):
        if False:
            pygame.draw.rect(self.display, [255, 0, 0], random.randint(5, self.width), random.randint(5, self.height))
