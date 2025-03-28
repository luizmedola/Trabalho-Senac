# -*- coding: utf-8 -*-
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton, QWidget

class Ui_Cadastro(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 720)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #FEF8E8;\n"
                                 "border-radius: 2px")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Components Setup
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(30, 0, 131, 121))
        self.logo.setStyleSheet(u"opacity: 0.2;")
        self.logo.setPixmap(QPixmap(u"image/Logo.png"))
        
        self.Taskzen = QLabel(self.centralwidget)
        self.Taskzen.setObjectName(u"Taskzen")
        self.Taskzen.setGeometry(QRect(160, 40, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"Montserrat SemiBold"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.Taskzen.setFont(font1)
        self.Taskzen.setStyleSheet(u"color: #1F3043")
        
        self.Cadastro = QLabel(self.centralwidget)
        self.Cadastro.setObjectName(u"Cadastro")
        self.Cadastro.setGeometry(QRect(468, 130, 191, 61))
        font2 = QFont()
        font2.setFamilies([u"Montserrat ExtraBold"])
        font2.setPointSize(22)
        self.Cadastro.setFont(font2)
        self.Cadastro.setStyleSheet(u"color: #E33C2A")
        self.Cadastro.setAlignment(Qt.AlignCenter)
        
        self.txt_usuario = QLabel(self.centralwidget)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(250, 210, 151, 61))
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setPointSize(18)
        self.txt_usuario.setFont(font3)
        self.txt_usuario.setStyleSheet(u"color: #1F3043;")
        
        self.txt_email = QLabel(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(270, 310, 151, 61))
        self.txt_email.setFont(font3)
        self.txt_email.setStyleSheet(u"color: #1F3043;")
        
        self.txt_password = QLabel(self.centralwidget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(260, 400, 151, 61))
        self.txt_password.setFont(font3)
        self.txt_password.setStyleSheet(u"color: #1F3043;")
        
        self.txt_password2 = QLabel(self.centralwidget)
        self.txt_password2.setObjectName(u"txt_password2")
        self.txt_password2.setGeometry(QRect(130, 480, 211, 61))
        self.txt_password2.setFont(font3)
        self.txt_password2.setStyleSheet(u"color: #1F3043;")
        
        self.img_frame = QLabel(self.centralwidget)
        self.img_frame.setObjectName(u"img_frame")
        self.img_frame.setGeometry(QRect(690, 280, 400, 400))
        self.img_frame.setStyleSheet(u"opacity: 10;")
        self.img_frame.setPixmap(QPixmap(u"image/itens_cadastro.png"))
        
        self.Cadastrar = QPushButton(self.centralwidget)
        self.Cadastrar.setObjectName(u"Cadastrar")
        self.Cadastrar.setGeometry(QRect(640, 580, 131, 31))
        font4 = QFont()
        font4.setFamilies([u"Montserrat ExtraBold"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.Cadastrar.setFont(font4)
        self.Cadastrar.setStyleSheet(u"background: #E33C2A;\n"
                                      "color: white;\n"
                                      "border-radius: 5px;")
        
        self.Voltar = QPushButton(self.centralwidget)
        self.Voltar.setObjectName(u"Voltar")
        self.Voltar.setGeometry(QRect(370, 580, 131, 31))
        self.Voltar.setFont(font4)
        self.Voltar.setStyleSheet(u"background: #1F3043;\n"
                                  "color: white;\n"
                                  "border-radius: 5px;")
        
        self.user_input = QLineEdit(self.centralwidget)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(360, 230, 381, 31))
        self.user_input.setStyleSheet(u"border: 1px solid #D2D2D2;\n"
                                      "padding-left: 10px;\n"
                                      "background: white;\n"
                                      "border-radius: 5")
        
        self.email_input = QLineEdit(self.centralwidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(360, 320, 381, 31))
        self.email_input.setStyleSheet(u"border: 1px solid #D2D2D2;\n"
                                       "padding-left: 10px;\n"
                                       "background: white;\n"
                                       "border-radius: 5")
        
        self.senha_input = QLineEdit(self.centralwidget)
        self.senha_input.setObjectName(u"senha_input")
        self.senha_input.setGeometry(QRect(360, 410, 381, 31))
        self.senha_input.setStyleSheet(u"border: 1px solid #D2D2D2;\n"
                                       "padding-left: 10px;\n"
                                       "background: white;\n"
                                       "border-radius: 5;")
        self.senha_input.setEchoMode(QLineEdit.Password)
        
        self.senha2_input = QLineEdit(self.centralwidget)
        self.senha2_input.setObjectName(u"senha2_input")
        self.senha2_input.setGeometry(QRect(360, 500, 381, 31))
        self.senha2_input.setStyleSheet(u"border: 1 solid #D2D2D2;\n"
                                        "padding-left: 10px;\n"
                                        "background: white;\n"
                                        "border-radius: 5;")
        self.senha2_input.setEchoMode(QLineEdit.Password)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.img_frame.raise_()
        self.logo.raise_()
        self.Taskzen.raise_()
        self.Cadastro.raise_()
        self.txt_usuario.raise_()
        self.txt_email.raise_()
        self.txt_password.raise_()
        self.txt_password2.raise_()
        self.Cadastrar.raise_()
        self.Voltar.raise_()
        self.user_input.raise_()
        self.email_input.raise_()
        self.senha_input.raise_()
        self.senha2_input.raise_()
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.Taskzen.setText(QCoreApplication.translate("MainWindow", u"T A S K Z E N", None))
        self.Cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRO", None))
        self.txt_usuario.setText(QCoreApplication.translate("MainWindow", u"Usuário:", None))
        self.txt_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.txt_password.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.txt_password2.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha:", None))
        self.img_frame.setText("")
        self.Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.Voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.user_input.setText("")
        self.user_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"exemplo123...", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"exemplo@hotmail.com", None))