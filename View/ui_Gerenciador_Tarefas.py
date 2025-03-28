# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class Ui_GerenciadorTarefas(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Kanban")
        MainWindow.setGeometry(100, 100, 1000, 700)
        
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.layout_principal = QVBoxLayout(self.centralwidget)
        
        self.barra_superior = QWidget()
        self.layout_barra = QHBoxLayout(self.barra_superior)
        self.barra_superior.setFixedHeight(30)
        self.barra_superior.setStyleSheet("QWidget { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FEF8E8, stop:1 #F4E4BC); border-bottom: 1px solid #22354B; }")
        
        self.label_titulo = QLabel("Kanban")
        self.label_titulo.setStyleSheet("QLabel { color: #22354B; font-size: 12px; padding-left: 5px; }")
        
        self.botao_adicionar_tarefa = QPushButton("Adicionar Tarefa")
        self.botao_excluir_tarefa = QPushButton("Excluir Tarefa")
        self.botao_editar_tarefa = QPushButton("Editar Tarefa")
        self.botao_detalhes = QPushButton("Ver Detalhes")
        
        estilo_botao = "QPushButton { background-color: #22354B; color: #FEF8E8; padding: 4px 10px; border: 1px solid #22354B; border-radius: 2px; font-size: 12px; } QPushButton:hover { background-color: #D9A05B; }"
        self.botao_adicionar_tarefa.setStyleSheet(estilo_botao)
        self.botao_excluir_tarefa.setStyleSheet(estilo_botao)
        self.botao_editar_tarefa.setStyleSheet(estilo_botao)
        self.botao_detalhes.setStyleSheet(estilo_botao)
        
        self.layout_barra.addWidget(self.label_titulo)
        self.layout_barra.addStretch()
        self.layout_barra.addWidget(self.botao_adicionar_tarefa)
        self.layout_barra.addWidget(self.botao_excluir_tarefa)
        self.layout_barra.addWidget(self.botao_editar_tarefa)
        self.layout_barra.addWidget(self.botao_detalhes)
        self.layout_barra.setContentsMargins(0, 0, 5, 0)
        self.layout_principal.addWidget(self.barra_superior)
        
        self.layout_colunas = QHBoxLayout()
        self.layout_colunas.setSpacing(10)
        
        self.layout_principal.addLayout(self.layout_colunas)
        
        MainWindow.setStyleSheet("QMainWindow { background-color: #FEF8E8; }")