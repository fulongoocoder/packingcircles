__author__ = 'chenzd'

from PyQt4 import QtGui
from MyMainWindow import MyMainWindow

import sys
app = QtGui.QApplication(sys.argv)
pmw = MyMainWindow()
pmw.pack()
pmw.show()
app.exec()



