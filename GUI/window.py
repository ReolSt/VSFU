# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI\window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 132)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UpdateLocalFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateLocalFileButton.setGeometry(QtCore.QRect(10, 10, 191, 41))
        self.UpdateLocalFileButton.setObjectName("UpdateLocalFileButton")
        self.UpdateDriveFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateDriveFileButton.setGeometry(QtCore.QRect(240, 10, 181, 41))
        self.UpdateDriveFileButton.setObjectName("UpdateDriveFileButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 70, 71, 16))
        self.label.setObjectName("label")
        self.AutoUpdateCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.AutoUpdateCheckBox.setGeometry(QtCore.QRect(410, 70, 16, 16))
        self.AutoUpdateCheckBox.setText("")
        self.AutoUpdateCheckBox.setObjectName("AutoUpdateCheckBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionConfigures = QtWidgets.QAction(MainWindow)
        self.actionConfigures.setObjectName("actionConfigures")
        self.menuSettings.addAction(self.actionConfigures)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UpdateLocalFileButton.setText(_translate("MainWindow", "Update Local File"))
        self.UpdateDriveFileButton.setText(_translate("MainWindow", "Update Drive File"))
        self.label.setText(_translate("MainWindow", "Auto Update"))
        self.menuSettings.setTitle(_translate("MainWindow", "Options"))
        self.actionConfigures.setText(_translate("MainWindow", "Configure VDSS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
