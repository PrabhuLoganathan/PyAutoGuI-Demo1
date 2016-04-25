from PyQt4 import QtGui, QtCore
from py_file import Ui_MainWindow
import sys
from mySerial import Serial
import pyautogui as p


width, height = p.size()

pointer_speed = 10
scroll_speed = 5

class Gui(QtGui.QMainWindow):
    cmd_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.cmd_signal.connect(self.cmd_update)
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.scroll_speed.returnPressed.connect(self.update_scroll_speed)
        self.ui.pointer_speed.returnPressed.connect(self.update_pointer_speed)
        self.ui.com_port.returnPressed.connect(self.set_com)

    def set_com(self):
        th.com_change.emit()

    def disable_all(self):
        self.ui.left_arrow.setEnabled(False)   
        self.ui.right_arrow.setEnabled(False)
        self.ui.up_arrow.setEnabled(False)
        self.ui.down_arrow.setEnabled(False)
        self.ui.left_click.setEnabled(False)
        self.ui.right_click.setEnabled(False)
        self.ui.scroll_down.setEnabled(False)
        self.ui.scroll_up.setEnabled(False)

    def update_scroll_speed(self):
        global scroll_speed
        s = str(self.ui.scroll_speed.text())
        if s.isdigit():
            scroll_speed = int(s)
        else:
            self.ui.scroll_speed.setText('5')
            scroll_speed = 5

    def update_pointer_speed(self):
        global pointer_speed
        s = str(self.ui.pointer_speed.text())
        
        if s.isdigit():
            pointer_speed = int(s)
        else:
            self.ui.pointer_speed.setText('10')
            pointer_speed = 10


    def cmd_update(self,data):
        self.ui.cmd.setText(data)
        

class Worker(QtCore.QThread):
    quit_app = QtCore.pyqtSignal()
    com_change = QtCore.pyqtSignal()

    def __init__(self, gui_obj,parent=None):
        super(Worker, self).__init__()
        self.ser = Serial()
        self.gui = gui_obj
        self.com_change.connect(self.ser_update)

    def ser_update(self):
        self.ser.port = int(self.gui.ui.com_port.text())
        self.ser.open()
    
    def run(self):
        global scroll_speed
        global pointer_speed
        while True:
            data = self.ser.read()
            print data
            self.gui.cmd_signal.emit(data)
            if data == '7':
                # print "ABORTING !!"
                self.quit_app.emit()
                break
            
            elif data == '$':
                print "Left Click"
                try:
                    p.click(button = 'left')
                    self.gui.disable_all()
                    self.gui.ui.left_click.setEnabled(True)
                except Exception, e:
                    print e
            elif data == '#':
                print "Right Click"
                try:
                    p.click(button = 'right')
                    self.gui.disable_all()
                    self.gui.ui.right_click.setEnabled(True)
                except Exception, e:
                    print e
            elif data == 'L':
                print "Left Key"
                try:
                    p.moveRel(-1 * pointer_speed,0)
                    self.gui.disable_all()
                    self.gui.ui.left_arrow.setEnabled(True)
                except Exception,e:
                    print e
            elif data == 'R':
                print "Right Key"
                try:
                    p.moveRel(pointer_speed,0)
                    self.gui.disable_all()
                    self.gui.ui.right_arrow.setEnabled(True)
                except Exception, e:
                    print e
            elif data == 'D':
                print "Down key"
                try:
                    p.moveRel(0,pointer_speed)
                    self.gui.disable_all()
                    self.gui.ui.down_arrow.setEnabled(True)
                except Exception,e:
                    print e
            elif data == 'U':
                print "Up key"
                try:
                    p.moveRel(0,-1 * pointer_speed)
                    self.gui.disable_all()
                    self.gui.ui.up_arrow.setEnabled(True)
                except Exception,e:
                    print e
            elif data == '4':
                try:
                    p.scroll(scroll_speed)
                    self.gui.disable_all()
                    self.gui.ui.scroll_up.setEnabled(True)
                except Exception,e:
                    print e  
            elif data == '5':
                try:
                    p.scroll(-1 * scroll_speed)
                    self.gui.disable_all()
                    self.gui.ui.scroll_down.setEnabled(True)
                except Exception,e:
                    print e  
            else:
                print "Unknown cmd: ", data
            
        
def main():
    global th
    global app
    app = QtGui.QApplication(sys.argv)
    ex = Gui()
    ex.show()
    th = Worker(ex)
    th.start()
    th.quit_app.connect(app.exit)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
