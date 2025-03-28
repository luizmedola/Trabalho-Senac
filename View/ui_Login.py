# -*- coding: utf-8 -*-
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton, QWidget

class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1128, 720)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.Foto_fundo = QLabel(self.centralwidget)
        self.Foto_fundo.setObjectName(u"Foto_fundo")
        self.Foto_fundo.setGeometry(QRect(0, 0, 1131, 731))
        self.Foto_fundo.setPixmap(QPixmap(u"image/Tela_fundo_login.png"))
        self.Foto_fundo.setScaledContents(True)

        self.Foto_login = QLabel(self.centralwidget)
        self.Foto_login.setObjectName(u"Foto_login")
        self.Foto_login.setGeometry(QRect(290, 90, 521, 481))
        self.Foto_login.setPixmap(QPixmap(u"image/LOGIN_RETANGULO.png"))
        self.Foto_login.setScaledContents(True)

        self.Btn_voltar = QPushButton(self.centralwidget)
        self.Btn_voltar.setObjectName(u"Btn_voltar")
        self.Btn_voltar.setGeometry(QRect(350, 482, 111, 31))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(11)
        self.Btn_voltar.setFont(font)
        self.Btn_voltar.setStyleSheet(u"background: #2A95E3;\n"
                                      "border-radius: 5px;\n"
                                      "color: white;")

        self.Btn_entrar = QPushButton(self.centralwidget)
        self.Btn_entrar.setObjectName(u"Btn_entrar")
        self.Btn_entrar.setGeometry(QRect(650, 480, 111, 31))
        self.Btn_entrar.setFont(font)
        self.Btn_entrar.setStyleSheet(u"background: #E33C2A;\n"
                                      "border-radius: 5px;\n"
                                      "color: white;")

        self.lineEdit_usuario = QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setObjectName(u"lineEdit_usuario")
        self.lineEdit_usuario.setGeometry(QRect(420, 260, 311, 41))
        self.lineEdit_usuario.setStyleSheet(u"border-radius: 4px;\n"
                                            "border: 1.5px solid #D2D2D2;")
        self.lineEdit_usuario.setPlaceholderText("Email")

        self.lineEdit_senha = QLineEdit(self.centralwidget)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(420, 340, 311, 41))
        self.lineEdit_senha.setStyleSheet(u"border-radius: 4px;\n"
                                          "border: 1.5px solid #D2D2D2;")
        self.lineEdit_senha.setEchoMode(QLineEdit.Password)
        self.lineEdit_senha.setPlaceholderText("Senha")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Foto_fundo.setText("")
        self.Foto_login.setText("")
        self.Btn_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.Btn_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))