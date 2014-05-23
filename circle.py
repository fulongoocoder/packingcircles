__author__ = 'chenzd'

import math

class Circle:
    def __init__(self, r, x = 0, y = 0):
        self._x = x
        self._y = y
        self._r = r
        self._index = -1
        self.isin = False

    def setposition(self, x, y):
        """
        @param x:
        @param y:
        """
        self._x = x
        self._y = y

    def setindex(self, index):
        """d"""
        self._index = index

    def index(self):
        return self._index

    def x(self):
        return self._x

    def y(self):
        return self._y

    def center(self):
        return (self._x, self._y)

    def r(self):
        return  self._r

    def putin(self):
        self.isin = True

    def isputin(self):
        return self.isin

    def print(self):
        print("x = %f" % self._x)
        print("y = %f" % self._y)

    def iscontain(self, circle):
        """判断是否包含该圆"""
        dis = self.distance(self.center(), circle.center())
        if((self.r() - circle.r()) >= (dis - 0.0001)):
            return True
        else:
            return False

    def isoverlapped(self, circle):
        dis = self.distance(self.center(), circle.center())
        if((self.r() + circle.r()) > (dis + 0.0001)):
            return True
        else:
            return False

    def distance(self, pos1, pos2):
        x = pos1[0] - pos2[0]
        y = pos1[1] - pos2[1]
        return math.sqrt(x*x + y*y)

    def distanceto(self, circle):
        return self.distance(self.center(), circle.center())

    def vectorto(self, circle):
        x = circle.x() - self.x()
        y = circle.y() - self.y()
        return (x, y)


c1 = Circle(100, 0, 0)
c2 = Circle(19.99999, 0, 119)
if c1.iscontain(c2):
    print("contain")

if c1.isoverlapped(c2):
    print("ov")

print(c1.distanceto(c2))