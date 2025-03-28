# -*- coding: utf-8 -*-
import mysql.connector
from PySide6.QtCore import QDate, QSize
from PySide6.QtWidgets import (QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, 
                               QLabel, QPushButton, QMessageBox, QWidget, 
                               QListWidgetItem, QSpacerItem, QSizePolicy)
from View.ui_Projetos_Finalizados import Ui_ProjetosFinalizados

class Projetos_Finalizados(QMainWindow):
    def __init__(self, sessao_usuario, pai=None):
        super().__init__(pai)
        self.sessao_usuario = sessao_usuario
        self.ui = Ui_ProjetosFinalizados()
        self.ui.setupUi(self)
        
        self.atualizando = False
        self.atualizar_lista_projetos_finalizados()

        # Conexões dos botões
        self.ui.Button_Excluir_Projeto.clicked.connect(self.excluir_projeto_selecionado)
        self.ui.button_Sair.clicked.connect(self.close)
        self.ui.button_Projetos.clicked.connect(self.voltar_para_projetos)

    def atualizar_lista_projetos_finalizados(self):
        if not self.atualizando:
            self.atualizando = True
            self.ui.Projetos_Finalizados.clear()
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM projetos WHERE usuario_id = %s AND finalizado = TRUE", (self.sessao_usuario["id"],))
            projetos = cursor.fetchall()
            cursor.close()
            conexao.close()
            
            for projeto in projetos:
                item = QListWidgetItem()
                self.ui.Projetos_Finalizados.addItem(item)
                
                widget_cartao = QWidget()
                layout_cartao = QHBoxLayout(widget_cartao)
                layout_cartao.setContentsMargins(10, 10, 10, 10)
                
                label_nome = QLabel(projeto["nome"])
                label_nome.setStyleSheet(u"font-size: 16px; color: #22354B; border: none;")
                layout_cartao.addWidget(label_nome)
                
                layout_cartao.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
                
                label_finalizado = QLabel("Finalizado")
                label_finalizado.setStyleSheet(u"font-size: 14px; color: #FFFFFF; border: none;")
                layout_cartao.addWidget(label_finalizado)
                
                widget_cartao.setStyleSheet("background: #80A1C7;\n"
                                            "border: 1px solid #D2D2D2;\n"
                                            "border-radius: 5px;\n"
                                            "padding: 10px;")
                
                item.setSizeHint(QSize(0, 60))
                self.ui.Projetos_Finalizados.setItemWidget(item, widget_cartao)
            
            self.atualizando = False

    def excluir_projeto_selecionado(self):
        item_selecionado = self.ui.Projetos_Finalizados.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Aviso", "Selecione um projeto para excluir.")
            return

        nome_projeto_excluir = self.ui.Projetos_Finalizados.itemWidget(item_selecionado).findChild(QLabel, "").text()

        janela_dialogo = QDialog(self)
        janela_dialogo.setWindowTitle("Confirmação")
        layout_dialogo = QVBoxLayout()
        layout_dialogo.addWidget(QLabel(f"Deseja excluir o projeto finalizado '{nome_projeto_excluir}'?"))
        botao_sim = QPushButton("Sim")
        botao_nao = QPushButton("Não")
        layout_botoes = QHBoxLayout()
        layout_botoes.addWidget(botao_sim)
        layout_botoes.addWidget(botao_nao)
        layout_dialogo.addLayout(layout_botoes)

        botao_sim.clicked.connect(janela_dialogo.accept)
        botao_nao.clicked.connect(janela_dialogo.reject)
        janela_dialogo.setLayout(layout_dialogo)

        if janela_dialogo.exec():
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM projetos WHERE nome = %s AND usuario_id = %s AND finalizado = TRUE", 
                           (nome_projeto_excluir, self.sessao_usuario["id"]))
            conexao.commit()
            cursor.close()
            conexao.close()
            self.atualizar_lista_projetos_finalizados()

    def voltar_para_projetos(self):
        from Logica.Tela_Tarefas import Tela_Tarefas  # Importação local para evitar circularidade
        self.janela_projetos = Tela_Tarefas(self.sessao_usuario)
        self.janela_projetos.show()
        self.close()