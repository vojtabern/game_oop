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

    def move(self):
        if self.axis == "x":
            if self.xy + 107 >= self.display:
                self.xy = self.xy - self.step
                #change_tuple.Vector2[0].__add__(-5)
                return self.xy
            elif self.xy <= 0:
                self.xy = self.xy + self.step
                #change_tuple.Vector2[0].__add__(5)
                return self.xy
    #def move_y(self):
        elif self.axis == "y":
            if self.xy+99 >= self.display:
                self.xy = self.xy - self.step
                #change_tuple.Vector2[1].__add__(-5)
                return self.xy
            elif self.xy - 5 <= 0:
                self.xy = self.xy + self.step
                return self.xy
        return self.xy



