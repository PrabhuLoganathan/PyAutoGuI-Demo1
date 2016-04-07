from PyQt4 import QtGui, QtCore
from py_file import Ui_MainWindow
import sys
from mySerial import Serial
import pyautogui as p

width, height = p.size()


class Gui(QtGui.QMainWindow):
    cmd_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.cmd_signal.connect(self.cmd_update)
        self.ui.setupUi(self)

    def disable_all(self):
        self.ui.left_arrow.setEnabled(False)   
        self.ui.right_arrow.setEnabled(False)
        self.ui.up_arrow.setEnabled(False)
        self.ui.down_arrow.setEnabled(False)
        self.ui.left_click.setEnabled(False)
        self.ui.right_click.setEnabled(False)
        self.ui.scroll_down.setEnabled(False)
        self.ui.scroll_up.setEnabled(False)
    def cmd_update(self,data):
        self.ui.cmd.setText(data)
        

class Worker(QtCore.QThread):
    quit_app = QtCore.pyqtSignal()

    def __init__(self, gui_obj,parent=None):
        super(Worker, self).__init__()
        self.ser = Serial()
        self.gui = gui_obj
    
    def run(self):
        
        while True:
            data = self.ser.read()
            self.gui.cmd_signal.emit(data)
            if data == '7':
                # print "ABORTING !!"
                self.quit_app.emit()
                break
            
            elif data == '1':
                # print "Left Click"
                try:
                    p.click(button = 'left')
                    self.gui.disable_all()
                    self.gui.ui.left_click.setEnabled(True)
                except Exception, e:
                    print e
            elif data == '2':
                # print "Right Click"
                try:
                    p.click(button = 'right')
                    self.gui.disable_all()
                    self.gui.ui.right_click.setEnabled(True)
                except Exception, e:
                    print e
            elif data == 'a':
                # print "Left Key"
                try:
                    p.moveRel(-10,0)
                    self.gui.disable_all()
                    self.gui.ui.left_arrow.setEnabled(True)
                except Exception,e:
                    print e
            elif data == 'd':
                # print "Right Key"
                try:
                    p.moveRel(10,0)
                    self.gui.disable_all()
                    self.gui.ui.right_arrow.setEnabled(True)
                except Exception, e:
                    print e
            elif data == 's':
                # print "Down key"
                try:
                    p.moveRel(0,10)
                    self.gui.disable_all()
                    self.gui.ui.down_arrow.setEnabled(True)
                except Exception,e:
                    print e
            elif data == 'w':
                # print "Up key"
                try:
                    p.moveRel(0,-10)
                    self.gui.disable_all()
                    self.gui.ui.up_arrow.setEnabled(True)
                except Exception,e:
                    print e
            elif data == '4':
                try:
                    p.scroll(5)
                    self.gui.disable_all()
                    self.gui.ui.scroll_up.setEnabled(True)
                except Exception,e:
                    print e  
            elif data == '5':
                try:
                    p.scroll(-5)
                    self.gui.disable_all()
                    self.gui.ui.scroll_down.setEnabled(True)
                except Exception,e:
                    print e  
            else:
                print "Unknown cmd: ", data
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    th = Worker(ex)
    th.start()
    th.quit_app.connect(app.exit)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()