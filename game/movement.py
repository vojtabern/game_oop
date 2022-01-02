import pygame
class Movement:
    def __init__(self, default_x, default_y):
        self.x = default_x
        self.y = default_y
        self.step = 5
    def move(self):
        keys = pygame.key.get_pressed()
        if keys:
            if keys[pygame.K_w]:
                self.y -= self.step
                return self.y
            if keys[pygame.K_s]:
                self.y += self.step
                return self.y
            if keys[pygame.K_d]:
                self.x += self.step
                return self.x
            if keys[pygame.K_a]:
                self.x -= self.step
                return self.x


