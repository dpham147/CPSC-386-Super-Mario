import pygame


class Vector:

    GRAVITY = Vector(0, 20)

    def __init__(self, x, y): self.__x, self.__y = x, y

    @classmethod
    def create(cls, pta, ptb):       # create a Vector from pta to ptb
        x = ptb.x - pta.x
        y = ptb.y - pta.y
        return cls(x, y)

    def __str__(self): return 'Vector(' + str(self.x) + ',' + str(self.y) + ')'

    def getx(self): return self.__x

    def gety(self): return self.__y

    def setx(self, x): self.__x = x

    def sety(self, y): self.__y = y

    x = property(getx, setx)

    y = property(gety, sety)

    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other): return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float): return Vector(k * self.x, k * self.y)

    def __rmul__(self, k: float): return self.__mul__(k)

    def __neg__(self): return Vector(-self.x, -self.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __imul__(self, k: float):
        self.x *= k
        self.y *= k
        return self

    def dot(self, other): return self.x * other.x + self.y * other.y

    def draw(self, point, screen, color):
        pygame.draw.line(screen, color, point, (point.x + self.x, point.y + self.y), 5)
