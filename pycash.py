
import sys
from sample import Ui_Form
from PyQt4 import QtCore, QtGui


class Main(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def onClick(self):
        print 'kdkdkdkd'


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    ex.show()

    sys.exit(app.exec_())

