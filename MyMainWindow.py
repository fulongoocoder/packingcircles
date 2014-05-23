__author__ = 'chenzd'

from PyQt4 import QtGui
from PyQt4.QtCore import QPointF
from ui_mymainwindow import Ui_MyMainWindow
from circle import Circle
from packing import Packing

class MyMainWindow(QtGui.QMainWindow, Ui_MyMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.circles = []
        self.coners = []
        self.packing = Packing()
        self.brush = QtGui.QBrush(QtGui.QColor(255, 0 , 0))
    def paintEvent(self, *args, **kwargs):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(QtGui.QColor(0, 0, 0))
        for circle in self.circles:
            x = circle.x() + self.width()/2
            y = -1 * circle.y() + self.height()/2
            r = circle.r()
            painter.drawEllipse(QPointF(x, y), r, r)
            print(circle.index())
        painter.setPen(QtGui.QColor(255, 0, 0))
        for coner in self.coners:
            x, y = coner.pos()
            x += self.width()/2
            y = y * -1 + self.height()/2
            r = 20
            painter.drawEllipse(QPointF(x, y), r, r)
        painter.end()

    def addcircle(self,c):
        self.circles.append(c)

    def setconers(self, coners):
        self.coners = coners

    def pack(self):
        self.packing.addcirclecontaner(90)
        self.packing.addcircle(20)
        self.packing.addcircle(10)
        self.packing.addcircle(20)
        self.packing.addcircle(25)
        self.packing.addcircle(25)
        self.packing.addcircle(60)
        self.packing.addcircle(20)
        self.packing.addcircle(10)
        self.packing.addcircle(10)
        self.packing.addcircle(5)
        circles = self.packing.rund()
        for c in circles:
            c.print()
            self.addcircle(c)
        print("num of coners = %d" % len(self.packing.getconers()))
        self.setconers(self.packing.getconers())







