import pygame
#import display
import change_tuple


class Movement():
    def __init__(self,display, player, xy, axis):
        self.xy = xy
        self.display = display
        self.player = player
        self.step = 5
        self.axis = axis

    # def move(self):
    #     if self.axis == "x":
    #         if self.xy + 107 >= self.display:
    #             self.xy = self.xy - self.step
    #
    #             #change_tuple.Vector2[0].__add__(-5)
    #             return self.xy
    #         elif self.xy <= 0:
    #             self.xy = self.xy + self.step
    #             #change_tuple.Vector2[0].__add__(5)
    #             return self.xy
    #     elif self.axis == "y":
    #         if self.xy+99 >= self.display:
    #             self.xy = self.xy - self.step
    #             #change_tuple.Vector2[1].__add__(-5)
    #             return self.xy
    #         elif self.xy - 5 <= 0:
    #             self.xy = self.xy + self.step
    #             return self.xy
    #     return self.xy

    def control_x(self, vector):
        if self.axis == "x":
            if self.xy + 111 >= self.display and vector == 'd':
                return False
            elif self.xy - 4 <= 0 and vector == 'a':
                return False
        return True

    def control_y(self, vector):
        if self.axis == "y":
            if self.xy + 103 > self.display and vector == 's':
                return False
            elif self.xy -19 <= 0 and vector == 'w':
                return False
        return True
