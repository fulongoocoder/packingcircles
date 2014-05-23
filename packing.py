__author__ = 'chenzd'

from circle import Circle
import math
import itertools
from coner import Conner

class Packing():
    def __init__(self):
        self.circles = []
        self.l = []
        self.c = []

    def addcircle(self, r):
        """容器的index是0，所以需要排列的圆的index > 0 """
        cir = Circle(r)
        cir.setindex(len(self.circles))
        self.circles.append(cir)

    def addcirclecontaner(self, r):
        cir = Circle(r)
        self.c.append(cir)

    def configurationc(self):
        if len(self.circles) >2:
            contaner = self.c[0]
            cir = self.circles[0]
            x = 0
            conr = contaner.r()
            y = -1 * conr + cir.r()
            cir.putin()
            cir.setposition(x, y)
            self.c.append(cir)

            seccir = self.circles[1]
            b = contaner.r() - seccir.r()
            c = contaner.r() - cir.r()
            a = seccir.r() + cir.r()
            angle = self.angle(a, b, c)
            rat = b/c
            vec = self.rotate((x, y), angle)
            x1 = vec[0] * rat
            y1 = vec[1] * rat
            seccir.setposition(x1,y1)
            seccir.putin()
            self.c.append(seccir)

    def initconerlist(self):
        """此时定义coner1：由circlae[0]和contaner
        coner2: circles[0]-circles[1]
        coner32: circles[1]-container"""
        for c in self.circles:
            if(not c.isputin()):
                self.calculateconer(c)

    def calculateconer(self, circle):
        for com in itertools.combinations(range(len(self.c)), 2):
            #计算container有关的角
            if com[0] == 0:
                container = self.c[0]
                seconcir = self.c[com[1] ]
                self.calculatecontainerconer(circle, container, seconcir)
            else:
                circle1 = self.c[com[0] ]
                circle2 = self.c[com[1] ]
                self.calculatecirclesconer(circle, circle1,circle2)


    def calculatecontainerconer(self, circle, container, seconcir):
        a = seconcir.r() + circle.r()
        b = container.r() - circle.r()
        c = container.distanceto(seconcir)

        if (b > (a + c)) :
            return
        if (c > (a + b)):
            return
        if (a > (b + c)):
            return
        angle = self.angle(a, b, c)
        vec = (seconcir.x(), seconcir.y())
        vec1 = self.rotate(vec, angle)
        rat = b / c
        x1 = vec1[0] * rat
        y1 = vec1[1] * rat
        #检查该位置是否可以放置该圆
        if self.isfitconer((x1, y1), circle):
             self.l.append(Conner(circle.index(), x1, y1, container.index(), seconcir.index()))

        if(angle == 0):
            return
        angle *= -1
        vec1 = self.rotate(vec, angle)
        rat = b / c
        x1 = vec1[0] * rat
        y1 = vec1[1] * rat
        #检查该位置是否可以放置该圆
        if self.isfitconer((x1, y1), circle):
            self.l.append(Conner(circle.index(), x1, y1, container.index(), seconcir.index()))

    def calculatecirclesconer(self, circle, circle1, circle2):
        """计算两个圆之间的角"""
        a = circle2.r() + circle.r()
        b = circle1.r() + circle.r()
        c = circle2.distanceto(circle1)

        if(b > (a + c)):
            return
        if(c > (a + b)):
            return

        angle = self.angle(a, b, c)
        vec = circle1.vectorto(circle2)
        vec1 = self.rotate(vec, angle)
        rat = b/c
        x1 = vec1[0] * rat + circle1.x()
        y1 = vec1[1] * rat + circle1.y()
        if self.isfitconer((x1, y1), circle):
            self.l.append(Conner(circle.index(), x1, y1, circle1.index(), circle2.index()))

        if not angle:
            return
        angle *= -1
        vec1 = self.rotate(vec, angle)
        rat = b/c
        x1 = vec1[0] * rat + circle1.x()
        y1 = vec1[1] * rat + circle1.y()
        if self.isfitconer((x1, y1), circle):
            self.l.append(Conner(circle.index(), x1, y1, circle1.index(), circle2.index()))

    def isfitconer(self, pos, circle):
        circle.setposition(pos[0], pos[1])
        for c in self.c:
            if c.index() == -1:
                if not c.iscontain(circle):
                    return False
            else:
                if circle.isoverlapped(c):
                    return False
        return True



    def angle(self, a, b, c):
        """求边a对应的角"""
        value = (b*b+c*c-a*a)/(2*b*c)
        if abs(value) > 1:
            if (abs(value) - 1) < 0.0001:
                value = abs(value)/value;
            else:
                raise BaseException();

        angle = math.acos(value)
        return angle

    def rotate(self, vec, angle):
        x = vec[0]
        y = vec[1]
        x1 = x * math.cos(angle) - y * math.sin(angle)
        y1 = x * math.sin(angle) + y * math.cos(angle)
        return (x1, y1)

    def getconnertoplacecircle(self):
        maxlam = -100
        nexconner = None
        for conner in self.l:
            lam = self.benifit(conner)
            print("lam = %f" % lam)
            if lam > maxlam:
                maxlam = lam
                nexconner = conner
        return nexconner;

    def benifit(self, conner):
        mindim = self.c[0].r() * 2
        cir = self.circles[conner.index()]
        for circle in self.c:
            if circle.index() not in (conner.tangentcircles()):
                dis = circle.distance(circle.center(), (conner.pos()))
                if circle.index() == -1:
                    dim = circle.r() - cir.r() - dis
                    if dim < mindim:
                        mindim = dim
                else:
                    dim = dis - circle.r() - cir.r()
                    if dim < mindim:
                        mindim = dim
        lam = 1- dim/cir.r()
        return lam


    def updateconnerlist(self, circle):
        #delete all conners of circle
        ls = []
        for coner in self.l:
            if coner.index() != circle.index():  # not circle conner
                cir = self.circles[coner.index()]
                x, y = coner.pos()
                cir.setposition(x, y)
                if not circle.isoverlapped(cir):  # not overlapped with circle
                    ls.append(coner)
        # add new conners
        self.l = ls
        for cir in self.circles:
            container = self.c[0]
            if not cir.isputin():
                for seccir in self.c:
                        if seccir.index() == -1:
                            self.calculatecontainerconer(cir, container, circle)
                        elif seccir.index() != circle.index():
                            self.calculatecirclesconer(cir, circle, seccir)
    def rund(self):
        self.configurationc()
        self.initconerlist()
        conner = self.getconnertoplacecircle()
        while(conner):
            circle = self.circles[conner.index()]
            x, y = conner.pos()
            circle.setposition(x, y)
            circle.putin()
            self.c.append(circle)
            self.updateconnerlist(circle)
            conner = self.getconnertoplacecircle()


        return self.c

    def getconers(self):
        return self.l

pac = Packing()
pac.addcirclecontaner(100)
pac.addcircle(20)
pac.addcircle(10)
pac.rund()

angle = pac.angle(10, 20 , 30)