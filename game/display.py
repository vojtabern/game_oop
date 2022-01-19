
import pygame
import random
import movement
import pygame.freetype



class Display:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.max_x = 1000
        self.max_y = 500
        self.score = 0
        self.vector = 'd'
        self.width = 107
        self.height = 99
        self.max_score = 60


    def window(self):
        pygame.init()
        display = pygame.display.set_mode((self.max_x, self.max_y))
        pygame.display.set_caption("Game")
        fpsclock = pygame.time.Clock()
        draw_player = pygame.draw.rect(display, [255, 225, 0], pygame.Rect(self.x, self.y, self.width, self.height))
        apple_x = Spawn_food(display, self.max_x, self.max_y).spawn_destination('x')
        apple_y = Spawn_food(display, self.max_x, self.max_y).spawn_destination('y')
        font = pygame.font.Font('freesansbold.ttf', 32)

        running = True
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
                    if keys[pygame.K_s] and self.vector != 'w':
                        if self.vector != 's':
                            self.y = self.y +1
                            self.x = self.x + 0
                        self.vector = 's'
                        continue
                    if keys[pygame.K_d] and self.vector != 'a':
                        if self.vector != 'd':
                            self.y = self.y + 0
                            self.x = self.x + 1
                        self.vector = 'd'
                        continue
                    if keys[pygame.K_a] and self.vector != 'd':
                        if self.vector != 'a':
                            self.y = self.y + 0
                            self.x = self.x - 1
                        self.vector = 'a'
                        continue

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

            draw_player = pygame.draw.rect(display, [255, 225, 0], pygame.Rect(self.x, self.y, self.width, self.height))
            print(f"{self.score}")

            # score code




            if self.score > self.max_score:
                text = font.render('You are the winner!!', True, [255, 255, 150])
                textRect = text.get_rect()
                textRect.center = (self.max_x // 2, self.max_y // 2)
            else:
                text = font.render(f'Score: {self.score}', True, [255, 0, 0])
                textRect = text.get_rect()

            pygame.display.flip()

            display.blit(text, textRect)

            apple = Spawn_food(display, self.max_x, self.max_y).draw(apple_x, apple_y)
            if Eat(draw_player, apple).collision():
                self.score += 1
                if self.max_y > self.height and self.max_x > self.width:
                    self.height += 5
                    self.width += 5
                apple_x = Spawn_food(display, self.max_x, self.max_y).spawn_destination('x')
                apple_y = Spawn_food(display, self.max_x, self.max_y).spawn_destination('y')
            self.x = movement.Movement(self.max_x, draw_player, self.x, "x", self.width, self.height).move()
            self.y = movement.Movement(self.max_y, draw_player, self.y, "y", self.width, self.height).move()
            pygame.display.update()


class Spawn_food:
    def __init__(self, display, max_x, max_y):
        self.display = display
        self.max_x = max_x
        self.max_y = max_y

    def spawn_destination(self, axis):
        if axis == 'x':
            apple_xy: int = random.randrange(107, self.max_x - 50)
            return apple_xy
        elif axis == 'y':
            apple_xy: int = random.randrange(107, self.max_y - 50)
            return apple_xy

    def draw(self, apple_x, apple_y):
        apple = pygame.draw.rect(self.display, [255, 0, 0], pygame.Rect(apple_x, apple_y, 50, 50))
        return apple


class Eat:
    def __init__(self, draw_player, apple):
        self.apple = apple
        self.draw_player = draw_player

    def collision(self):
        if self.draw_player.colliderect(self.apple):
            return True
        return False


Display(250, 250).window()