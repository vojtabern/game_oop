import math
import random


class Create_body:
    def __init__(self, track, no_food, distance):
        self.track = track
        self.no_food = no_food
        self.distance = distance

    def create(self):
        body = [(self.track[0])]
        track_i = 1
        for i in range(1, self.no_food):
            while track_i < len(self.track):
                pos = self.track[track_i]
                track_i += 1
                dx, dy = body[-1][0]-pos[0], body[-1][1]-pos[1]
                if math.sqrt(dx*dx + dy*dy) >= self.distance:
                    body.append(pos)
                    break
        while len(body) < self.no_food:
            body.append(self.track[-1])
        return body





