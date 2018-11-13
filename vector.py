import pygame
from math import sqrt
from color import Color


class Vector:
    def __init__(self, x, y, z=0): self.__x, self.__y, self.__z = x, y, z

    @classmethod
    def create(cls, pta, ptb):       # create a Vector from pta to ptb
        x = ptb.x - pta.x
        y = ptb.y - pta.y
        z = ptb.z - pta.z
        return cls(x, y, z)

    def __str__(self): return 'Vector(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def xy(self): return (self.x, self.y)

    def xyint(self): return (int(self.x), int(self.y))

    def getx(self): return self.__x

    def gety(self): return self.__y

    def getz(self): return self.__z

    def setx(self, x): self.__x = x

    def sety(self, y): self.__y = y

    def setz(self, z): self.__z = z

    x = property(getx, setx)

    y = property(gety, sety)

    z = property(getz, setz)

    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other): return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, k): return Vector(k * self.x, k * self.y, k * self.z)

    def __rmul__(self, k): return self.__mul__(k)

    def __rdiv__(self, k): return Vector(self.x / k, self.y / k, self.z / k)

    def __neg__(self): return Vector(-self.x, -self.y, -self.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __imul__(self, k):
        self.x *= k
        self.y *= k
        self.z *= k
        return self

    def dot(self, other): return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def norm(self): return float(self.dot(self))

    def normalize(self, other):
        if other.magnitude() < 1e-19:
            # print("************************** not normalized")
            return self
        return self * (1.0 / other.magnitude())

    def magnitude(self): return sqrt(self.norm())

    def orthogonal(self, normal):     # ortho, unit vector to self in plane perpendicular to normal
        ortho = self.cross(normal)
        return ortho.normalize(ortho)

    def sign(self, other): return 1 if self.norm(other) > 0 else -1

    def draw(self, screen, origin, color=Color.GREEN, scale=5000, thickness=5):
        dest = origin + scale * self
        pygame.draw.line(screen, color, origin.xy(), dest.xy(), thickness)

        offset = self.magnitude() / 10.0
        delta = offset * ihat + jhat
        o = self.orthogonal(self.cross(delta))
        shorter = origin + (dest - origin) * 0.9
        mag = 10
        # print("o normalized is: " + str(o))
        # print("mag * o is: " + str(mag * o))
        lower = shorter + mag * o
        upper = shorter - mag * o

        pts = []
        pts.append(dest.xy())
        pts.append(lower.xy())
        pts.append(upper.xy())
        pygame.draw.polygon(screen, color, pts, thickness)

    def draw_xcomponent(self, game, origin, color=Color.GREEN, scale=5000, thickness=5):
        Vector(self.x, 0, 0).draw(game, origin, color, scale, thickness)

    def draw_ycomponent(self, game, origin, color=Color.GREEN, scale=5000, thickness=5):
        Vector(0, self.y, 0).draw(game, origin, color, scale, thickness)

    def draw_zcomponent(self, game, origin, color=Color.GREEN, scale=5000, thickness=5):
        Vector(0, 0, self.z).draw(game, origin, color, scale, thickness)

    def draw_components(self, game, origin, color=Color.GREEN, scale=5000, thickness=5):
        self.draw_xcomponent(game, origin, color, scale, thickness)
        self.draw_ycomponent(game, origin, color, scale, thickness)
        # self.draw_zcomponent(game, origin, color, scale, thickness)

    @staticmethod
    def forces():
        return Vector(.1, .15, 0)

ihat = Vector(1, 0, 0)
jhat = Vector(0, 1, 0)
khat = Vector(0, 0, 1)
zero_vec = Vector(0, 0, 0)
