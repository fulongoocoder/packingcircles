__author__ = 'chenzd'

class Conner:
    def __init__(self, index, x, y, tangentc1, tangentc2):
        self._index = index
        self._x = x
        self._y = y
        self._tangentcircle1 = tangentc1
        self._tangentcircle2 = tangentc2

    def index(self):
        return self._index

    def pos(self):
        return self._x, self._y

    def tangentcircles(self):
        return self._tangentcircle1, self._tangentcircle2