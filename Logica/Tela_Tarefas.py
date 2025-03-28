# -*- coding: utf-8 -*-
import mysql.connector
from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, QSize, QDate, QMimeData, QRect)
from PySide6.QtGui import (QFont, QPixmap, QCursor, QDrag)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QListWidget, QListWidgetItem, QMainWindow, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget,
                               QDialog, QLineEdit, QMessageBox, QDateEdit, QCheckBox,
                               QComboBox, QTextEdit, QFormLayout)
from View.ui_Tela_Tarefas import Ui_TelaTarefas
from Logica.Gerenciador_Tarefas import Gerenciador_Tarefas
from Logica.Gerenciador_Tarefas import Projeto

#from logico.gerenciador_tarefas import Projeto, Gerenciador_Tarefas

def iniciar_banco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="taskzen"
    )
    cursor = conexao.cursor()
    
    # cursor.execute("DROP DATABASE IF EXISTS taskzen")
    # cursor.execute("CREATE DATABASE taskzen")
    conexao.commit()
    cursor.close()
    conexao.close()
    
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="taskzen"
    )
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) NOT NULL UNIQUE,
            senha VARCHAR(100) NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projetos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario_id INT NOT NULL,
            nome VARCHAR(50) NOT NULL,
            data_inicio DATE NOT NULL,
            data_termino DATE NOT NULL,
            finalizado BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            projeto_id INT,
            usuario_id INT NOT NULL,
            nome VARCHAR(25) NOT NULL,
            categoria VARCHAR(50) NOT NULL,
            prioridade VARCHAR(50) NOT NULL,
            descricao TEXT NOT NULL,
            coluna VARCHAR(50) NOT NULL DEFAULT 'Em Planejamento',
            FOREIGN KEY (projeto_id) REFERENCES projetos(id) ON DELETE CASCADE,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
        )
    """)
    
    cursor.execute("INSERT IGNORE INTO usuarios (email, senha) VALUES ('teste@teste.com', '1234')")
    
    conexao.commit()
    cursor.close()
    conexao.close()

class Tela_Tarefas(QMainWindow):
    def __init__(self, sessao_usuario):
        super().__init__()
        self.sessao_usuario = sessao_usuario
        self.ui = Ui_TelaTarefas()
        self.ui.setupUi(self)
        
        iniciar_banco()
        self.atualizando = False
        self.atualizar_lista_projetos()
        

        self.ui.Button_Adicionar_Projeto.clicked.connect(self.criar_novo_projeto)
        self.ui.Button_Editar_Projeto.clicked.connect(self.editar_projeto_selecionado)
        self.ui.Button_Excluir_Projeto.clicked.connect(self.excluir_projeto_selecionado)
        self.ui.Button_Finalizar_Projeto.clicked.connect(self.finalizar_projeto_selecionado)
        self.ui.button_Finalizados.clicked.connect(self.abrir_projetos_finalizados)

        self.ui.button_Sair.clicked.connect(self.close)
        self.ui.Projeto.itemSelectionChanged.connect(self.tratar_mudanca_selecao)
        self.ui.Projeto.itemDoubleClicked.connect(self.abrir_kanban)
    def abrir_projetos_finalizados(self):
            from Logica.Projetos_Finalizados import Projetos_Finalizados  # Importação local para evitar circularidade
            self.janela_finalizados = Projetos_Finalizados(self.sessao_usuario, self)
            self.janela_finalizados.show()
            self.hide()
    def tratar_mudanca_selecao(self):
        if not self.atualizando:
            self.atualizando = True
            item_selecionado = self.ui.Projeto.currentItem()
            for i in range(self.ui.Projeto.count()):
                item = self.ui.Projeto.item(i)
                widget_cartao = self.ui.Projeto.itemWidget(item)
                nome_projeto = widget_cartao.findChild(QLabel, "").text()
                conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="taskzen"
                )
                cursor = conexao.cursor(dictionary=True)
                cursor.execute("SELECT finalizado FROM projetos WHERE nome = %s AND usuario_id = %s", (nome_projeto, self.sessao_usuario["id"]))
                finalizado = cursor.fetchone()["finalizado"]
                cursor.close()
                conexao.close()
                
                if item_selecionado == item:
                    cor_cartao = "#D3D3D3"
                else:
                    cor_cartao = "#80A1C7" if finalizado else "white"
                
                widget_cartao.setStyleSheet(f"background: {cor_cartao};\n"
                                           "border: 1px solid #D2D2D2;\n"
                                           "border-radius: 5px;\n"
                                           "padding: 10px;")
            self.atualizando = False

    def atualizar_lista_projetos(self):
        if not self.atualizando:
            self.atualizando = True
            self.ui.Projeto.clear()
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taskzen"
        )
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM projetos WHERE usuario_id = %s", (self.sessao_usuario["id"],))
        projetos = cursor.fetchall()
        cursor.close()
        conexao.close()
        
        for projeto in projetos:
            item = QListWidgetItem()
            self.ui.Projeto.addItem(item)
            
            widget_cartao = QWidget()
            layout_cartao = QHBoxLayout(widget_cartao)
            layout_cartao.setContentsMargins(10, 10, 10, 10)
            
            label_nome = QLabel(projeto["nome"])
            label_nome.setStyleSheet(u"font-size: 16px; color: #22354B; border: none;")
            layout_cartao.addWidget(label_nome)
            
            layout_cartao.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            
            if not projeto["finalizado"]:
                # Corrigir o formato da data para "yyyy-MM-dd" (padrão do MySQL)
                data_termino = QDate.fromString(str(projeto["data_termino"]), "yyyy-MM-dd")
                dias = QDate.currentDate().daysTo(data_termino)
                if dias >= 0:
                    texto_dias = f"{dias} dias restantes"
                    estilo_dias = u"font-size: 14px; color: #2A95E3; border: none;"
                else:
                    texto_dias = f"{-dias} dias atrasado"
                    estilo_dias = u"font-size: 14px; color: #E33C2A; border: none;"
                label_dias = QLabel(texto_dias)
                label_dias.setStyleSheet(estilo_dias)
                layout_cartao.addWidget(label_dias)
            else:
                label_finalizado = QLabel("Finalizado")
                label_finalizado.setStyleSheet(u"font-size: 14px; color: #FFFFFF; border: none;")
                layout_cartao.addWidget(label_finalizado)
            
            cor_cartao = "#80A1C7" if projeto["finalizado"] else "white"
            widget_cartao.setStyleSheet(f"background: {cor_cartao};\n"
                                       "border: 1px solid #D2D2D2;\n"
                                       "border-radius: 5px;\n"
                                       "padding: 10px;")
            
            item.setSizeHint(QSize(0, 60))
            self.ui.Projeto.setItemWidget(item, widget_cartao)
        
        self.atualizando = False
        self.tratar_mudanca_selecao()

    def criar_novo_projeto(self):
        janela_dialogo = QDialog(self)
        janela_dialogo.setWindowTitle("Novo Projeto")
        layout_dialogo = QVBoxLayout()
        
        label_nome = QLabel("Nome do Projeto (máx. 50 caracteres):")
        layout_dialogo.addWidget(label_nome)
        entrada_nome = QLineEdit()
        entrada_nome.setMaxLength(50)
        layout_dialogo.addWidget(entrada_nome)
        
        label_inicio = QLabel("Data de Início:")
        layout_dialogo.addWidget(label_inicio)
        entrada_data_inicio = QDateEdit()
        entrada_data_inicio.setCalendarPopup(True)
        entrada_data_inicio.setDate(QDate(2025, 3, 24))
        layout_dialogo.addWidget(entrada_data_inicio)
        
        label_termino = QLabel("Data de Término:")
        layout_dialogo.addWidget(label_termino)
        entrada_data_termino = QDateEdit()
        entrada_data_termino.setCalendarPopup(True)
        entrada_data_termino.setDate(QDate(2025, 3, 24))
        layout_dialogo.addWidget(entrada_data_termino)
        
        layout_botoes = QHBoxLayout()
        botao_salvar = QPushButton("Salvar")
        layout_botoes.addWidget(botao_salvar)
        botao_cancelar = QPushButton("Cancelar")
        layout_botoes.addWidget(botao_cancelar)
        layout_dialogo.addLayout(layout_botoes)

        def validar_e_salvar():
            nome = entrada_nome.text().strip()
            if not nome:
                QMessageBox.warning(janela_dialogo, "Aviso", "O campo 'Nome do Projeto' não pode estar vazio.")
                return
            if entrada_data_termino.date() <= entrada_data_inicio.date():
                QMessageBox.warning(janela_dialogo, "Erro", "A data de término deve ser posterior à data de início.")
                return
            
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM projetos WHERE nome = %s AND usuario_id = %s", (nome, self.sessao_usuario["id"]))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(janela_dialogo, "Erro", "Já existe um projeto com esse nome para este usuário.")
                cursor.close()
                conexao.close()
                return
            cursor.close()
            conexao.close()
            
            janela_dialogo.accept()

        botao_salvar.clicked.connect(validar_e_salvar)
        botao_cancelar.clicked.connect(janela_dialogo.reject)
        janela_dialogo.setLayout(layout_dialogo)

        if janela_dialogo.exec():
            nome = entrada_nome.text().strip()
            data_inicio = entrada_data_inicio.date().toString("yyyy-MM-dd")
            data_termino = entrada_data_termino.date().toString("yyyy-MM-dd")
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO projetos (usuario_id, nome, data_inicio, data_termino) VALUES (%s, %s, %s, %s)",
                           (self.sessao_usuario["id"], nome, data_inicio, data_termino))
            conexao.commit()
            cursor.close()
            conexao.close()
            self.atualizar_lista_projetos()

    def editar_projeto_selecionado(self):
        item_selecionado = self.ui.Projeto.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Aviso", "Selecione um projeto para editar.")
            return

        nome_projeto_atual = self.ui.Projeto.itemWidget(item_selecionado).findChild(QLabel, "").text()
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taskzen"
        )
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM projetos WHERE nome = %s AND usuario_id = %s", (nome_projeto_atual, self.sessao_usuario["id"]))
        projeto = cursor.fetchone()
        cursor.close()
        conexao.close()

        janela_dialogo = QDialog(self)
        janela_dialogo.setWindowTitle("Editar Projeto")
        layout_dialogo = QVBoxLayout()
        
        label_nome = QLabel("Nome do Projeto (máx. 50 caracteres):")
        layout_dialogo.addWidget(label_nome)
        entrada_nome = QLineEdit(projeto["nome"])
        entrada_nome.setMaxLength(50)
        layout_dialogo.addWidget(entrada_nome)
        
        label_inicio = QLabel("Data de Início:")
        layout_dialogo.addWidget(label_inicio)
        entrada_data_inicio = QDateEdit()
        entrada_data_inicio.setCalendarPopup(True)
        entrada_data_inicio.setDate(QDate.fromString(str(projeto["data_inicio"]), "yyyy-MM-dd"))
        layout_dialogo.addWidget(entrada_data_inicio)
        
        label_termino = QLabel("Data de Término:")
        layout_dialogo.addWidget(label_termino)
        entrada_data_termino = QDateEdit()
        entrada_data_termino.setCalendarPopup(True)
        entrada_data_termino.setDate(QDate.fromString(str(projeto["data_termino"]), "yyyy-MM-dd"))
        layout_dialogo.addWidget(entrada_data_termino)
        
        layout_botoes = QHBoxLayout()
        botao_salvar = QPushButton("Salvar")
        layout_botoes.addWidget(botao_salvar)
        botao_cancelar = QPushButton("Cancelar")
        layout_botoes.addWidget(botao_cancelar)
        layout_dialogo.addLayout(layout_botoes)

        
        def validar_e_salvar():
            nome = entrada_nome.text().strip()
            if not nome:
                QMessageBox.warning(janela_dialogo, "Aviso", "O campo 'Nome do Projeto' não pode estar vazio.")
                return
            if entrada_data_termino.date() <= entrada_data_inicio.date():
                QMessageBox.warning(janela_dialogo, "Erro", "A data de término deve ser posterior à data de início.")
                return
            
            if nome != nome_projeto_atual:
                conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="taskzen"
                )
                cursor = conexao.cursor()
                cursor.execute("SELECT COUNT(*) FROM projetos WHERE nome = %s AND usuario_id = %s", (nome, self.sessao_usuario["id"]))
                if cursor.fetchone()[0] > 0:
                    QMessageBox.warning(janela_dialogo, "Erro", "Já existe um projeto com esse nome para este usuário.")
                    cursor.close()
                    conexao.close()
                    return
                cursor.close()
                conexao.close()
            
            janela_dialogo.accept()

        botao_salvar.clicked.connect(validar_e_salvar)
        botao_cancelar.clicked.connect(janela_dialogo.reject)
        janela_dialogo.setLayout(layout_dialogo)

        if janela_dialogo.exec():
            nome = entrada_nome.text().strip()
            data_inicio = entrada_data_inicio.date().toString("yyyy-MM-dd")
            data_termino = entrada_data_termino.date().toString("yyyy-MM-dd")
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()
            cursor.execute("UPDATE projetos SET nome = %s, data_inicio = %s, data_termino = %s WHERE id = %s",
                           (nome, data_inicio, data_termino, projeto["id"]))
            conexao.commit()
            cursor.close()
            conexao.close()
            self.atualizar_lista_projetos()

    def excluir_projeto_selecionado(self):
        item_selecionado = self.ui.Projeto.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Aviso", "Selecione um projeto para excluir.")
            return

        nome_projeto_excluir = self.ui.Projeto.itemWidget(item_selecionado).findChild(QLabel, "").text()

        janela_dialogo = QDialog(self)
        janela_dialogo.setWindowTitle("Confirmação")
        layout_dialogo = QVBoxLayout()
        layout_dialogo.addWidget(QLabel(f"Deseja excluir o projeto '{nome_projeto_excluir}'?"))
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
            cursor.execute("DELETE FROM projetos WHERE nome = %s AND usuario_id = %s", (nome_projeto_excluir, self.sessao_usuario["id"]))
            conexao.commit()
            cursor.close()
            conexao.close()
            self.atualizar_lista_projetos()

    def finalizar_projeto_selecionado(self):
        item_selecionado = self.ui.Projeto.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Aviso", "Selecione um projeto para finalizar.")
            return

        nome_projeto_finalizar = self.ui.Projeto.itemWidget(item_selecionado).findChild(QLabel, "").text()
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taskzen"
        )
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id, finalizado FROM projetos WHERE nome = %s AND usuario_id = %s", (nome_projeto_finalizar, self.sessao_usuario["id"]))
        projeto = cursor.fetchone()
        id_projeto = projeto["id"]
        finalizado = projeto["finalizado"]
        
        if finalizado:
            cursor.close()
            conexao.close()
            QMessageBox.information(self, "Aviso", "Esse projeto já está finalizado.")
            return
        
        cursor.execute("SELECT COUNT(*) as total FROM tarefas WHERE projeto_id = %s AND usuario_id = %s AND coluna != 'Concluído'", 
                       (id_projeto, self.sessao_usuario["id"]))
        tarefas_pendentes = cursor.fetchone()["total"]
        cursor.close()
        conexao.close()

        if tarefas_pendentes > 0:
            QMessageBox.warning(self, "Aviso", "O projeto só pode ser finalizado quando todas as tarefas estiverem concluídas.")
            return

        janela_dialogo = QDialog(self)
        janela_dialogo.setWindowTitle("Confirmação")
        layout_dialogo = QVBoxLayout()
        layout_dialogo.addWidget(QLabel(f"Deseja finalizar o projeto '{nome_projeto_finalizar}'?"))
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
            cursor.execute("UPDATE projetos SET finalizado = TRUE WHERE nome = %s AND usuario_id = %s", 
                           (nome_projeto_finalizar, self.sessao_usuario["id"]))
            conexao.commit()
            cursor.close()
            conexao.close()
            self.atualizar_lista_projetos()

    def abrir_kanban(self, item):
        nome_projeto = self.ui.Projeto.itemWidget(item).findChild(QLabel, "").text()
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taskzen"
        )
    
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM projetos WHERE nome = %s AND usuario_id = %s", (nome_projeto, self.sessao_usuario["id"]))
        dados_projeto = cursor.fetchone()
        cursor.close()
        conexao.close()
        
        if dados_projeto["finalizado"]:
            QMessageBox.information(self, "Aviso", "Este projeto já está finalizado e não pode ser editado.")
            return
        
        projeto = Projeto(dados_projeto["id"],
                         dados_projeto["nome"],
                         QDate.fromString(str(dados_projeto["data_inicio"]), "dd-MM-yyyy"),
                         QDate.fromString(str(dados_projeto["data_termino"]), "dd-MM-yyyy"),
                         dados_projeto["finalizado"])
        self.janela_kanban = Gerenciador_Tarefas(projeto, self.sessao_usuario, self)
        self.janela_kanban.show()