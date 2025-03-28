# -*- coding: utf-8 -*-
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QPixmap, QCursor
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QListWidget, 
                               QPushButton, QSizePolicy, QSpacerItem, 
                               QVBoxLayout, QWidget, QMainWindow)

class Ui_TelaTarefas(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1196, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: #FEF8E8")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        
        self.menu = QFrame(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(250, 0))
        self.menu.setMaximumSize(QSize(280, 16777215))
        self.menu.setStyleSheet(u"background-color: #22354B;\n"
                                "border-radius: 10px;")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.frame_7 = QFrame(self.menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        
        self.menu_logo = QFrame(self.frame_7)
        self.menu_logo.setObjectName(u"menu_logo")
        self.menu_logo.setMaximumSize(QSize(16777215, 150))
        self.menu_logo.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.menu_logo)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.img_logo = QLabel(self.menu_logo)
        self.img_logo.setObjectName(u"img_logo")
        self.img_logo.setMaximumSize(QSize(50, 16777215))
        self.img_logo.setPixmap(QPixmap(u"image/Logo.png"))  # Ajuste o caminho conforme necessário
        self.horizontalLayout_5.addWidget(self.img_logo)

        self.txt_Taskzen = QLabel(self.menu_logo)
        self.txt_Taskzen.setObjectName(u"txt_Taskzen")
        fonte = QFont()
        fonte.setPointSize(18)
        self.txt_Taskzen.setFont(fonte)
        self.txt_Taskzen.setStyleSheet(u"color: white;")
        self.horizontalLayout_5.addWidget(self.txt_Taskzen)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3.addWidget(self.menu_logo)

        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        
        self.menu_content = QFrame(self.frame_2)
        self.menu_content.setObjectName(u"menu_content")
        self.menu_content.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.menu_content)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        
        self.frame_11 = QFrame(self.menu_content)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        
        self.menu_content_space = QFrame(self.frame_11)
        self.menu_content_space.setObjectName(u"menu_content_space")
        self.menu_content_space.setMaximumSize(QSize(16777215, 80))
        self.menu_content_space.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6.addWidget(self.menu_content_space)

        self.menu_content_button = QFrame(self.frame_11)
        self.menu_content_button.setObjectName(u"menu_content_button")
        self.menu_content_button.setMaximumSize(QSize(16777215, 200))
        self.menu_content_button.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.menu_content_button)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        
        self.button_Projetos = QPushButton(self.menu_content_button)
        self.button_Projetos.setObjectName(u"button_Projetos")
        self.button_Projetos.setMaximumSize(QSize(16777215, 100))
        fonte1 = QFont()
        fonte1.setPointSize(15)
        self.button_Projetos.setFont(fonte1)
        self.button_Projetos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_Projetos.setStyleSheet(u"color: white;")
        self.verticalLayout_7.addWidget(self.button_Projetos)

        self.button_Finalizados = QPushButton(self.menu_content_button)
        self.button_Finalizados.setObjectName(u"button_Finalizados")
        self.button_Finalizados.setMaximumSize(QSize(16777215, 100))
        self.button_Finalizados.setFont(fonte1)
        self.button_Finalizados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_Finalizados.setStyleSheet(u"color: white;")
        self.verticalLayout_7.addWidget(self.button_Finalizados)

        self.verticalLayout_6.addWidget(self.menu_content_button)

        self.frame_15 = QFrame(self.menu_content)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6.addWidget(self.frame_15)

        self.verticalLayout_5.addWidget(self.frame_11)

        self.menu_content_sair = QFrame(self.menu_content)
        self.menu_content_sair.setObjectName(u"menu_content_sair")
        self.menu_content_sair.setMaximumSize(QSize(16777215, 100))
        self.menu_content_sair.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.menu_content_sair)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        
        self.button_Sair = QPushButton(self.menu_content_sair)
        self.button_Sair.setObjectName(u"button_Sair")
        self.button_Sair.setMinimumSize(QSize(0, 50))
        self.button_Sair.setFont(fonte1)
        self.button_Sair.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_Sair.setStyleSheet(u"color: white;")
        self.horizontalLayout_6.addWidget(self.button_Sair)

        self.verticalLayout_5.addWidget(self.menu_content_sair)

        self.verticalLayout_4.addWidget(self.menu_content)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.horizontalLayout_2.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(800, 0))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.Bar_title = QFrame(self.frame_3)
        self.Bar_title.setObjectName(u"Bar_title")
        self.Bar_title.setMaximumSize(QSize(16777215, 30))
        self.Bar_title.setStyleSheet(u"background: #22354B;\n"
                                     "border-radius: 4px;")
        self.Bar_title.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.Bar_title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.label = QLabel(self.Bar_title)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        fonte2 = QFont()
        fonte2.setPointSize(12)
        self.label.setFont(fonte2)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout.addWidget(self.Bar_title)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 600))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        
        self.Projeto = QListWidget(self.frame_6)
        self.Projeto.setObjectName(u"Projeto")
        self.Projeto.setStyleSheet(u"border: 1px solid #D2D2D2;\n"
                                   "border-radius: 10px;\n"
                                   "background: #FEF8E8;")
        self.Projeto.setSpacing(10)
        self.horizontalLayout_4.addWidget(self.Projeto)

        self.verticalLayout.addWidget(self.frame_6)

        self.Frame_Button = QFrame(self.frame_3)
        self.Frame_Button.setObjectName(u"Frame_Button")
        self.Frame_Button.setMinimumSize(QSize(0, 60))
        self.Frame_Button.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.Frame_Button)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSpacing(10)
        
        self.horizontalLayout_8.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self.Button_Excluir_Projeto = QPushButton(self.Frame_Button)
        self.Button_Excluir_Projeto.setObjectName(u"Button_Excluir_Projeto")
        self.Button_Excluir_Projeto.setFixedSize(QSize(150, 40))
        self.Button_Excluir_Projeto.setStyleSheet(u"background-color: #E33C2A;\n"
                                                  "color: white;\n"
                                                  "border-radius: 3px;\n"
                                                  "font-size: 14px;")
        self.horizontalLayout_8.addWidget(self.Button_Excluir_Projeto)

        self.Button_Editar_Projeto = QPushButton(self.Frame_Button)
        self.Button_Editar_Projeto.setObjectName(u"Button_Editar_Projeto")
        self.Button_Editar_Projeto.setFixedSize(QSize(150, 40))
        self.Button_Editar_Projeto.setStyleSheet(u"background-color: #22354B;\n"
                                                 "color: white;\n"
                                                 "border-radius: 3px;\n"
                                                 "font-size: 14px;")
        self.horizontalLayout_8.addWidget(self.Button_Editar_Projeto)

        self.Button_Finalizar_Projeto = QPushButton(self.Frame_Button)
        self.Button_Finalizar_Projeto.setObjectName(u"Button_Finalizar_Projeto")
        self.Button_Finalizar_Projeto.setFixedSize(QSize(150, 40))
        self.Button_Finalizar_Projeto.setStyleSheet(u"background-color: #28A745;\n"
                                                    "color: white;\n"
                                                    "border-radius: 3px;\n"
                                                    "font-size: 14px;")
        self.horizontalLayout_8.addWidget(self.Button_Finalizar_Projeto)

        self.Button_Adicionar_Projeto = QPushButton(self.Frame_Button)
        self.Button_Adicionar_Projeto.setObjectName(u"Button_Adicionar_Projeto")
        self.Button_Adicionar_Projeto.setFixedSize(QSize(150, 40))
        self.Button_Adicionar_Projeto.setStyleSheet(u"background-color: #2A95E3;\n"
                                                    "color: white;\n"
                                                    "border-radius: 3px;\n"
                                                    "font-size: 14px;")
        self.horizontalLayout_8.addWidget(self.Button_Adicionar_Projeto)

        self.horizontalLayout_8.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self.verticalLayout.addWidget(self.Frame_Button)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.horizontalLayout_7.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        #self.img_logo.setText("")
        self.txt_Taskzen.setText(QCoreApplication.translate("MainWindow", u"Taskzen", None))
        self.button_Projetos.setText(QCoreApplication.translate("MainWindow", u"Projetos", None))
        self.button_Finalizados.setText(QCoreApplication.translate("MainWindow", u"Projetos Finalizados", None))
        self.button_Sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Em Planejamento", None))
        self.Button_Excluir_Projeto.setText(QCoreApplication.translate("MainWindow", u"Excluir Projeto", None))
        self.Button_Editar_Projeto.setText(QCoreApplication.translate("MainWindow", u"Editar Projeto", None))
        self.Button_Finalizar_Projeto.setText(QCoreApplication.translate("MainWindow", u"Finalizar Projeto", None))
        self.Button_Adicionar_Projeto.setText(QCoreApplication.translate("MainWindow", u"Adicionar Projeto", None))