# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from styleTransfer import StyleTransfer

class Ui_MainWindow(object):
    def __init__(self):
        self.contentImage, self.styleImage = "", ""
        self.i = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 540)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelImageContent = QtWidgets.QLabel(self.centralwidget)
        self.labelImageContent.setGeometry(QtCore.QRect(50, 30, 221, 311))
        self.labelImageContent.setText("")
        self.labelImageContent.setObjectName("labelImageContent")
        self.labelImageStyle = QtWidgets.QLabel(self.centralwidget)
        self.labelImageStyle.setGeometry(QtCore.QRect(410, 30, 221, 311))
        self.labelImageStyle.setText("")
        self.labelImageStyle.setObjectName("labelImageStyle")
        self.buttonContent = QtWidgets.QPushButton(self.centralwidget)
        self.buttonContent.setGeometry(QtCore.QRect(100, 380, 101, 23))
        self.buttonContent.setObjectName("buttonContent")
        self.buttonStyle = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStyle.setGeometry(QtCore.QRect(465, 380, 101, 23))
        self.buttonStyle.setObjectName("buttonStyle")
        self.buttonTransfer = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTransfer.setGeometry(QtCore.QRect(290, 440, 111, 23))
        self.buttonTransfer.setObjectName("buttonTransfer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.buttonTransfer.setEnabled(False)
        self.buttonContent.clicked.connect(self.loadContent)
        self.buttonStyle.clicked.connect(self.loadStyle)
        self.buttonTransfer.clicked.connect(self.toTransfer)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadContent(self):
        fpath = QFileDialog.getOpenFileName(caption="Open File", filter="Image Files (*.png *.jpg *.jpeg)")[0]
        self.contentImage = fpath
        if len(self.contentImage)>0:
            self.buttonContent.setEnabled(False)
            pixmap = QPixmap(fpath)
            pixmap_resized = pixmap.scaled(299, 299, QtCore.Qt.KeepAspectRatio)
            self.labelImageContent.setPixmap(pixmap_resized)
            if len(self.contentImage)>0 and len(self.styleImage)>0:
                self.buttonTransfer.setEnabled(True)

    def loadStyle(self):
        fpath = QFileDialog.getOpenFileName(caption="Open File", filter="Image Files (*.png *.jpg *.jpeg)")[0]
        self.styleImage = fpath
        if len(self.styleImage)>0:
            self.buttonStyle.setEnabled(False)
            pixmap = QPixmap(fpath)
            pixmap_resized = pixmap.scaled(299, 299, QtCore.Qt.KeepAspectRatio)
            self.labelImageStyle.setPixmap(pixmap_resized)
            if len(self.contentImage)>0 and len(self.styleImage)>0:
                self.buttonTransfer.setEnabled(True) 
            
    def toTransfer(self):
        sTransfer = StyleTransfer(self.contentImage, self.styleImage)
        sTransfer.transfer(self.i)
        self.buttonTransfer.setEnabled(False)
        self.buttonContent.setEnabled(True)
        self.buttonStyle.setEnabled(True)
        self.i += 1
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NST - Designer                                          Made for best designer in the world :)"))
        self.buttonContent.setText(_translate("MainWindow", "Content Image"))
        self.buttonStyle.setText(_translate("MainWindow", "Style Image"))
        self.buttonTransfer.setText(_translate("MainWindow", "Hokus pokus :)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
