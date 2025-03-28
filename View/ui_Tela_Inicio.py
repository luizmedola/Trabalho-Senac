# -*- coding: utf-8 -*-
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel, QMainWindow, QPushButton, QWidget

class Ui_TelaInicio(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1128, 720)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #FEF8E8")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(30, 0, 131, 121))
        self.logo.setStyleSheet(u"opacity: 0.2;")
        self.logo.setPixmap(QPixmap("image/Logo.png"))
        
        self.Taskzen = QLabel(self.centralwidget)
        self.Taskzen.setObjectName(u"Taskzen")
        self.Taskzen.setGeometry(QRect(160, 40, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"Montserrat ExtraBold"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.Taskzen.setFont(font1)
        self.Taskzen.setStyleSheet(u"color: #1F3043")
        
        self.Texto1 = QLabel(self.centralwidget)
        self.Texto1.setObjectName(u"Texto1")
        self.Texto1.setGeometry(QRect(60, 260, 361, 71))
        font2 = QFont()
        font2.setFamilies([u"Montserrat ExtraBold"])
        font2.setPointSize(31)
        font2.setBold(True)
        self.Texto1.setFont(font2)
        self.Texto1.setStyleSheet("color: #1F3043; \n text-rendering: optimizeLegibility; \n")
        
        self.E33C2A = QLabel(self.centralwidget)
        self.E33C2A.setObjectName(u"E33C2A")
        self.E33C2A.setGeometry(QRect(60, 320, 281, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat ExtraBold"])
        font3.setPointSize(30)
        self.E33C2A.setFont(font3)
        self.E33C2A.setStyleSheet("color: #E33C2A; \n font-weight: bold; \n text-rendering: optimizeLegibility; \n")
        
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 390, 501, 21))
        font4 = QFont()
        font4.setFamilies([u"Montserrat Light"])
        font4.setPointSize(13)
        font4.setBold(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: #22354B")
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 410, 531, 20))
        font5 = QFont()
        font5.setFamilies([u"Montserrat Light"])
        font5.setPointSize(13)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: #22354B")
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 430, 261, 16))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: #22354B")
        
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 70, 700, 700))
        self.label_4.setPixmap(QPixmap("image/samurai_Login"))
        
        self.Login = QPushButton(self.centralwidget)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(83, 484, 131, 31))
        font6 = QFont()
        font6.setFamilies([u"Montserrat"])
        font6.setPointSize(12)
        self.Login.setFont(font6)
        self.Login.setStyleSheet(u"QPushButton {\n"
                                 "    color: white;\n"
                                 "    background: #E33C2A;\n"
                                 "    font-weight: bold; \n"
                                 "    border-radius: 5px; \n"
                                 "}")
        
        self.Cadastrar = QPushButton(self.centralwidget)
        self.Cadastrar.setObjectName(u"Cadastrar")
        self.Cadastrar.setGeometry(QRect(350, 480, 131, 31))
        self.Cadastrar.setFont(font6)
        self.Cadastrar.setStyleSheet(u"QPushButton{\n"
                                     "    background: #E33C2A;\n"
                                     "    font-weight: bold; \n"
                                     "    border-radius: 5px;\n"
                                     "    color: white;\n"
                                     "    text-rendering: optimizeLegibility; \n"
                                     "}")
        
        self.Login2 = QPushButton(self.centralwidget)
        self.Login2.setObjectName(u"Login2")
        self.Login2.setGeometry(QRect(950, 40, 131, 31))
        self.Login2.setFont(font6)
        self.Login2.setStyleSheet(u"QPushButton{\n"
                                  "    background: #E33C2A;\n"
                                  "    font-weight: bold; \n"
                                  "    border-radius: 5px;\n"
                                  "    color: white;\n"
                                  "}")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.logo.raise_()
        self.Taskzen.raise_()
        self.Texto1.raise_()
        self.E33C2A.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.Login.raise_()
        self.Cadastrar.raise_()
        self.Login2.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.Taskzen.setText(QCoreApplication.translate("MainWindow", u"T A S K Z E N", None))
        self.Texto1.setText(QCoreApplication.translate("MainWindow", u"Planeje-se como ", None))
        self.E33C2A.setText(QCoreApplication.translate("MainWindow", u"um Samurai", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Planeje, organize e realize seus objetivos de forma simples e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"eficiente. Transforme sua rotina em uma jornada de conquistas, ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"onde cada momento conta. ", None))
        self.label_4.setText("")
        self.Login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.Login2.setText(QCoreApplication.translate("MainWindow", u"Login", None))