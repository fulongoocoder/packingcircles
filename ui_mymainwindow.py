# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\5-program_practice\3-python\packingCircles/mymainwindow.ui'
#
# Created: Wed May 21 12:41:42 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MyMainWindow(object):
    def setupUi(self, MyMainWindow):
        MyMainWindow.setObjectName(_fromUtf8("MyMainWindow"))
        MyMainWindow.resize(467, 378)
        self.centralwidget = QtGui.QWidget(MyMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MyMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MyMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MyMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MyMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MyMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MyMainWindow)

    def retranslateUi(self, MyMainWindow):
        MyMainWindow.setWindowTitle(_translate("MyMainWindow", "PackingCircles", None))

