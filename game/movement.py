import pygame
#import display
import change_tuple


class Movement():
    def __init__(self, xy, m_xy):
        self.xy = xy
        self.m_xy = m_xy
        self.step = 5

    def move(self):
        if self.xy[0]+15 >= self.m_xy[0]:
            self.xy = self.xy[0] - self.step
            #change_tuple.Vector2[0].__add__(-5)
            return self.xy
        elif self.xy[0] - 15 <= 0:
            self.xy = self.xy[0] + self.step
            #change_tuple.Vector2[0].__add__(5)
            return self.xy

    #def move_y(self):
        elif self.xy[1]+15 >= self.m_xy[1]:
            self.xy = self.xy[1] - self.step
            #change_tuple.Vector2[1].__add__(-5)
            return self.xy
        elif self.xy[1] - 100 <= 0:
            # self.xy = self.xy[1] + self.step
            #change_tuple.Vector2.__add__(self.step)
            return self.xy
        return self.xy



