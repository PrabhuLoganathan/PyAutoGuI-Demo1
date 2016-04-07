from PyQt4 import QtGui, QtCore
from py_file import Ui_MainWindow
import sys


class Gui(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()