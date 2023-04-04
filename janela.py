# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 727)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.TXT_Path = QLineEdit(self.frame)
        self.TXT_Path.setObjectName(u"TXT_Path")
        font1 = QFont()
        font1.setPointSize(18)
        self.TXT_Path.setFont(font1)
        self.TXT_Path.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.TXT_Path)

        self.Button_Open = QPushButton(self.frame)
        self.Button_Open.setObjectName(u"Button_Open")
        font2 = QFont()
        font2.setPointSize(20)
        self.Button_Open.setFont(font2)

        self.verticalLayout_2.addWidget(self.Button_Open)

        self.Button_Organize = QPushButton(self.frame)
        self.Button_Organize.setObjectName(u"Button_Organize")
        font3 = QFont()
        font3.setPointSize(24)
        self.Button_Organize.setFont(font3)

        self.verticalLayout_2.addWidget(self.Button_Organize)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">ATLAS FILE MANAGER</span></p></body></html>", None))
        self.TXT_Path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta para organizar", None))
        self.Button_Open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.Button_Organize.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
    # retranslateUi

