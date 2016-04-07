# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_file.ui'
#
# Created: Thu Apr  7 13:30:10 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(247, 258)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.right_arrow = QtGui.QToolButton(self.gridLayoutWidget)
        self.right_arrow.setEnabled(False)
        self.right_arrow.setText(_fromUtf8(""))
        self.right_arrow.setArrowType(QtCore.Qt.RightArrow)
        self.right_arrow.setObjectName(_fromUtf8("right_arrow"))
        self.gridLayout.addWidget(self.right_arrow, 2, 5, 1, 1)
        self.line_3 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 3, 1)
        self.scroll_up = QtGui.QToolButton(self.gridLayoutWidget)
        self.scroll_up.setEnabled(False)
        self.scroll_up.setText(_fromUtf8(""))
        self.scroll_up.setArrowType(QtCore.Qt.UpArrow)
        self.scroll_up.setObjectName(_fromUtf8("scroll_up"))
        self.gridLayout.addWidget(self.scroll_up, 1, 1, 1, 1)
        self.scroll_down = QtGui.QToolButton(self.gridLayoutWidget)
        self.scroll_down.setEnabled(False)
        self.scroll_down.setText(_fromUtf8(""))
        self.scroll_down.setArrowType(QtCore.Qt.DownArrow)
        self.scroll_down.setObjectName(_fromUtf8("scroll_down"))
        self.gridLayout.addWidget(self.scroll_down, 3, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 6, 3, 1)
        self.line = QtGui.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 2, 3, 1)
        self.up_arrow = QtGui.QToolButton(self.gridLayoutWidget)
        self.up_arrow.setEnabled(False)
        self.up_arrow.setText(_fromUtf8(""))
        self.up_arrow.setArrowType(QtCore.Qt.UpArrow)
        self.up_arrow.setObjectName(_fromUtf8("up_arrow"))
        self.gridLayout.addWidget(self.up_arrow, 1, 4, 1, 1)
        self.down_arrow = QtGui.QToolButton(self.gridLayoutWidget)
        self.down_arrow.setEnabled(False)
        self.down_arrow.setText(_fromUtf8(""))
        self.down_arrow.setArrowType(QtCore.Qt.DownArrow)
        self.down_arrow.setObjectName(_fromUtf8("down_arrow"))
        self.gridLayout.addWidget(self.down_arrow, 3, 4, 1, 1)
        self.line_5 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 4, 0, 1, 7)
        self.line_4 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 0, 0, 1, 7)
        self.left_arrow = QtGui.QToolButton(self.gridLayoutWidget)
        self.left_arrow.setEnabled(False)
        self.left_arrow.setText(_fromUtf8(""))
        self.left_arrow.setArrowType(QtCore.Qt.LeftArrow)
        self.left_arrow.setObjectName(_fromUtf8("left_arrow"))
        self.gridLayout.addWidget(self.left_arrow, 2, 3, 1, 1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 170, 211, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cmd = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.cmd.setEnabled(False)
        self.cmd.setObjectName(_fromUtf8("cmd"))
        self.horizontalLayout_2.addWidget(self.cmd)
        self.left_click = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.left_click.setEnabled(False)
        self.left_click.setObjectName(_fromUtf8("left_click"))
        self.horizontalLayout_2.addWidget(self.left_click)
        self.right_click = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.right_click.setEnabled(False)
        self.right_click.setObjectName(_fromUtf8("right_click"))
        self.horizontalLayout_2.addWidget(self.right_click)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 247, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mouse", None))
        self.left_click.setText(_translate("MainWindow", "Left", None))
        self.right_click.setText(_translate("MainWindow", "Right", None))

