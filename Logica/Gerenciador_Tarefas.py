# -*- coding: utf-8 -*-
import mysql.connector
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag
from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, QSize, QDate, QMimeData, QRect)
from PySide6.QtGui import (QFont, QPixmap, QCursor, QDrag)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QListWidget, QListWidgetItem, QMainWindow, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget,
                               QDialog, QLineEdit, QMessageBox, QDateEdit, QCheckBox,
                               QComboBox, QTextEdit, QFormLayout)
from View.ui_Gerenciador_Tarefas import Ui_GerenciadorTarefas


class Projeto:
    def __init__(self, id, nome, data_inicio, data_termino, finalizado=False):
        self.id = id
        self.nome = nome[:50]
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.finalizado = finalizado
        self.tarefas = []

class Widget_Item_Tarefa(QWidget):
    def __init__(self, texto, pai=None):
        super().__init__(pai)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        
        self.widget_info = QWidget()
        layout_info = QHBoxLayout(self.widget_info)
        layout_info.setContentsMargins(5, 5, 5, 5)
        
        self.checkbox = QCheckBox()
        self.checkbox.clicked.connect(self.garantir_selecao_unica)
        layout_info.addWidget(self.checkbox)
        
        nome, categoria, prioridade = texto.split("\n")[:3]
        self.label_tarefa = QLabel(f"Tarefa: {nome}\n{categoria}\n{prioridade}")
        self.label_tarefa.setWordWrap(True)
        self.label_tarefa.setStyleSheet("QLabel { color: #22354B; }")
        layout_info.addWidget(self.label_tarefa)
        layout_info.addStretch()
        
        self.widget_info.setStyleSheet("QWidget { background-color: #FEF8E8; border: 1px solid #22354B; border-radius: 3px; padding: 5px; }")
        
        self.layout.addWidget(self.widget_info)
        self.setLayout(self.layout)

    def garantir_selecao_unica(self):
        if self.checkbox.isChecked():
            lista_pai = self.parent().parent()
            for i in range(lista_pai.count()):
                item = lista_pai.item(i)
                widget = lista_pai.itemWidget(item)
                if widget != self and widget.checkbox.isChecked():
                    widget.checkbox.setChecked(False)

class TaskCard(QListWidget):
    def __init__(self):
        super().__init__()
        self.setDragEnabled(True)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setStyleSheet("QListWidget { border: none; padding: 5px; background-color: transparent; }")

    def startDrag(self, supportedActions):
        item = self.currentItem()
        if item:
            mime_data = QMimeData()
            mime_data.setText(self.itemWidget(item).label_tarefa.text())
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            resultado = drag.exec(Qt.MoveAction)
            if resultado == Qt.MoveAction:
                self.takeItem(self.row(item))

    def adicionar_item_tarefa(self, texto):
        item = QListWidgetItem()
        widget = Widget_Item_Tarefa(texto)
        item.setSizeHint(widget.sizeHint())
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
        self.addItem(item)
        self.setItemWidget(item, widget)

class Coluna_Tarefa(QWidget):
    def __init__(self, titulo):
        super().__init__()
        self.setAcceptDrops(True)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        label = QLabel(titulo)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("QLabel { color: #FFFFFF; font-size: 14px; font-weight: bold; padding: 8px; background-color: #22354B; border-bottom: 1px solid #22354B; }")
        layout.addWidget(label)
        
        self.widget_lista = TaskCard()
        layout.addWidget(self.widget_lista)
        
        self.setLayout(layout)
        self.setStyleSheet("QWidget { background-color: #F4E4BC; border: 1px solid #22354B; border-radius: 4px; padding: 5px; } QWidget:focus { border: 2px solid #D9A05B; background-color: #FEF8E8; }")
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFixedWidth(250)
        self.setMinimumHeight(400)

    def dragEnterEvent(self, evento):
        if evento.mimeData().hasText():
            evento.acceptProposedAction()

    def dragMoveEvent(self, evento):
        if evento.mimeData().hasText():
            evento.acceptProposedAction()

    def dropEvent(self, evento):
        if evento.mimeData().hasText():
            origem = evento.source()
            texto = evento.mimeData().text()
            if origem != self.widget_lista:
                self.widget_lista.adicionar_item_tarefa(texto.replace("Tarefa: ", ""))
                nome = texto.split("\n")[0].replace("Tarefa: ", "")
                try:
                    conexao = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="taskzen"
                    )
                    cursor = conexao.cursor()
                    cursor.execute("UPDATE tarefas SET coluna = %s WHERE nome = %s AND projeto_id = %s AND usuario_id = %s",
                                   (self.findChild(QLabel).text(), nome, self.parent().parent().projeto.id, self.parent().parent().sessao_usuario["id"]))
                    conexao.commit()
                except mysql.connector.Error as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao atualizar tarefa: {e}")
                finally:
                    if conexao.is_connected():
                        cursor.close()
                        conexao.close()
                evento.acceptProposedAction()
            else:
                evento.ignore()

class Dialogo_Adicionar_Categoria(QDialog):
    def __init__(self, pai=None):
        super().__init__(pai)
        self.setWindowTitle("Adicionar Nova Categoria")
        self.setMinimumSize(250, 150)

        layout = QFormLayout()

        self.entrada_nome = QLineEdit()
        self.entrada_nome.setMaxLength(50)
        self.entrada_nome.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout.addRow("Nome da Categoria:", self.entrada_nome)

        botao_adicionar = QPushButton("Adicionar")
        botao_adicionar.clicked.connect(self.validar_e_aceitar)
        layout.addWidget(botao_adicionar)

        self.setLayout(layout)

        self.setStyleSheet("""
            QDialog { background-color: #FEF8E8; color: #22354B; }
            QLineEdit { background-color: #FFFFFF; color: #22354B; border: 1px solid #22354B; padding: 4px; border-radius: 2px; }
            QPushButton { background-color: #22354B; color: #FEF8E8; padding: 6px; border: 1px solid #22354B; border-radius: 3px; }
            QPushButton:hover { background-color: #D9A05B; }
        """)

    def validar_e_aceitar(self):
        nome = self.entrada_nome.text().strip()
        if not nome:
            QMessageBox.warning(self, "Aviso", "O campo 'Nome da Categoria' não pode estar vazio.")
            return
        self.accept()

    def obter_nome_categoria(self):
        return self.entrada_nome.text().strip()

class Dialogo_Adicionar_Tarefa(QDialog):
    def __init__(self, pai=None, editar_tarefa=None, nome="", categoria="", prioridade="", descricao=""):
        super().__init__(pai)
        self.setWindowTitle("Adicionar Nova Tarefa" if not editar_tarefa else "Editar Tarefa")
        self.setMinimumSize(300, 300)
        
        layout = QFormLayout()
        
        self.entrada_nome = QLineEdit()
        self.entrada_nome.setMaxLength(25)
        self.entrada_nome.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.entrada_descricao = QTextEdit()
        self.entrada_descricao.setFixedHeight(100)
        
        self.combo_categoria = QComboBox()
        self.carregar_categorias()  # Carrega as categorias do banco
        
        self.combo_prioridade = QComboBox()
        self.combo_prioridade.addItems(["Normal", "Opcional", "Crítica"])
        
        if editar_tarefa:
            self.entrada_nome.setText(nome)
            self.combo_categoria.setCurrentText(categoria)
            self.combo_prioridade.setCurrentText(prioridade)
            self.entrada_descricao.setText(descricao)
        
        layout.addRow("Nome da Tarefa:", self.entrada_nome)
        layout.addRow("Descrição:", self.entrada_descricao)
        layout.addRow("Categoria:", self.combo_categoria)
        layout.addRow("Prioridade:", self.combo_prioridade)
        
        botao_adicionar = QPushButton("Adicionar" if not editar_tarefa else "Salvar")
        botao_adicionar.clicked.connect(self.validar_e_aceitar)
        
        layout.addWidget(botao_adicionar)
        self.setLayout(layout)
        
        self.setStyleSheet("""
            QDialog { background-color: #FEF8E8; color: #22354B; }
            QLineEdit, QComboBox, QTextEdit { background-color: #FFFFFF; color: #22354B; border: 1px solid #22354B; padding: 4px; border-radius: 2px; }
            QPushButton { background-color: #22354B; color: #FEF8E8; padding: 6px; border: 1px solid #22354B; border-radius: 3px; }
            QPushButton:hover { background-color: #D9A05B; }
        """)

    def carregar_categorias(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()
            cursor.execute("SELECT nome FROM categorias WHERE usuario_id = %s", (self.parent().sessao_usuario["id"],))
            categorias = cursor.fetchall()
            self.combo_categoria.clear()
            if categorias:
                for categoria in categorias:
                    self.combo_categoria.addItem(categoria[0])
            else:
                self.combo_categoria.addItem("Nenhuma categoria disponível")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar categorias: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def validar_e_aceitar(self):
        nome = self.entrada_nome.text().strip()
        descricao = self.entrada_descricao.toPlainText().strip()
        if not nome or not descricao:
            QMessageBox.warning(self, "Aviso", "Os campos 'Nome da Tarefa' e 'Descrição' não podem estar vazios.")
            return
        self.accept()

    def obter_dados_tarefa(self):
        return (self.entrada_nome.text(),
                self.combo_categoria.currentText(),
                self.combo_prioridade.currentText(),
                self.entrada_descricao.toPlainText())

class Gerenciador_Tarefas(QMainWindow):
    def __init__(self, projeto, sessao_usuario, pai=None):
        super().__init__(pai)
        self.projeto = projeto
        self.sessao_usuario = sessao_usuario
        self.ui = Ui_GerenciadorTarefas()
        self.ui.setupUi(self)
        
        self.ui.label_titulo.setText(f"Kanban - {projeto.nome}")
        
        self.ui.botao_adicionar_tarefa.clicked.connect(self.mostrar_dialogo_adicionar_tarefa)
        self.ui.botao_excluir_tarefa.clicked.connect(self.excluir_tarefa)
        self.ui.botao_editar_tarefa.clicked.connect(self.editar_tarefa)
        self.ui.botao_detalhes.clicked.connect(self.mostrar_detalhes_tarefa)
        
        # Novo botão para adicionar categorias
        self.ui.botao_adicionar_categoria = QPushButton("Adicionar Categoria")
        self.ui.botao_adicionar_categoria.clicked.connect(self.mostrar_dialogo_adicionar_categoria)
        
        # Tentar adicionar ao mesmo layout do botão "Adicionar Tarefa"
        if hasattr(self.ui, 'layout_botoes'):  # Verifica se existe um layout de botões
            self.ui.layout_botoes.addWidget(self.ui.botao_adicionar_categoria)
        else:
            # Se não houver um layout específico, adicionar ao layout pai do botão "Adicionar Tarefa"
            layout_pai = self.ui.botao_adicionar_tarefa.parent().layout()
            if layout_pai and isinstance(layout_pai, QHBoxLayout):
                layout_pai.addWidget(self.ui.botao_adicionar_categoria)
            else:
                # Última tentativa: criar um novo layout horizontal e reposicionar os botões
                layout_botoes = QHBoxLayout()
                layout_botoes.addWidget(self.ui.botao_adicionar_tarefa)
                layout_botoes.addWidget(self.ui.botao_adicionar_categoria)
                layout_botoes.addWidget(self.ui.botao_excluir_tarefa)
                layout_botoes.addWidget(self.ui.botao_editar_tarefa)
                layout_botoes.addWidget(self.ui.botao_detalhes)
                self.ui.layout_colunas.addLayout(layout_botoes)  # Adiciona ao layout principal

        # Definir o estilo da janela principal
        self.setStyleSheet("""
            QMainWindow { 
                background-color: #FEF8E8; 
                color: #22354B; 
            }
            QDialog { 
                background-color: #FEF8E8; 
                color: #22354B; 
            }
            QLineEdit, QComboBox, QTextEdit { 
                background-color: #FFFFFF; 
                color: #22354B; 
                border: 1px solid #22354B; 
                padding: 4px; 
                border-radius: 2px; 
            }
            QPushButton { 
                background-color: #22354B; 
                color: #FEF8E8; 
                padding: 6px; 
                border: 1px solid #22354B; 
                border-radius: 3px; 
            }
            QPushButton:hover { 
                background-color: #D9A05B; 
            }
            QPushButton:disabled { 
                background-color: #CCCCCC; 
                color: #666666; 
            }
        """)
        
        # Garantir que o widget central tenha o fundo correto
        self.centralWidget().setStyleSheet("background-color: #FEF8E8;")
        
        # Aplicar estilo explicitamente ao botão "Adicionar Categoria"
        self.ui.botao_adicionar_categoria.setStyleSheet("""
            QPushButton { 
                background-color: #22354B; 
                color: #FEF8E8; 
                padding: 6px; 
                border: 1px solid #22354B; 
                border-radius: 3px; 
            }
            QPushButton:hover { 
                background-color: #D9A05B; 
            }
        """)
        
        self.lista_planejamento = Coluna_Tarefa("Em Planejamento")
        self.lista_progresso = Coluna_Tarefa("Em Progresso")
        self.lista_teste = Coluna_Tarefa("Teste")
        self.lista_concluido = Coluna_Tarefa("Concluído")
        
        self.ui.layout_colunas.addWidget(self.lista_planejamento)
        self.ui.layout_colunas.addWidget(self.lista_progresso)
        self.ui.layout_colunas.addWidget(self.lista_teste)
        self.ui.layout_colunas.addWidget(self.lista_concluido)
        
        self.carregar_tarefas_projeto()

    def carregar_tarefas_projeto(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tarefas WHERE projeto_id = %s AND usuario_id = %s", (self.projeto.id, self.sessao_usuario["id"]))
            self.projeto.tarefas = cursor.fetchall()
            
            for tarefa in self.projeto.tarefas:
                texto_tarefa = f"{tarefa['nome']}\nCategoria: {tarefa['categoria']}\nPrioridade: {tarefa['prioridade']}"
                if tarefa["coluna"] == "Em Planejamento":
                    self.lista_planejamento.widget_lista.adicionar_item_tarefa(texto_tarefa)
                elif tarefa["coluna"] == "Em Progresso":
                    self.lista_progresso.widget_lista.adicionar_item_tarefa(texto_tarefa)
                elif tarefa["coluna"] == "Teste":
                    self.lista_teste.widget_lista.adicionar_item_tarefa(texto_tarefa)
                elif tarefa["coluna"] == "Concluído":
                    self.lista_concluido.widget_lista.adicionar_item_tarefa(texto_tarefa)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar tarefas: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def mostrar_dialogo_adicionar_tarefa(self):
        dialogo = Dialogo_Adicionar_Tarefa(self)
        if dialogo.exec():
            nome, categoria, prioridade, descricao = dialogo.obter_dados_tarefa()
            self.adicionar_tarefa(nome, categoria, prioridade, descricao)

    def mostrar_dialogo_adicionar_categoria(self):
        dialogo = Dialogo_Adicionar_Categoria(self)
        if dialogo.exec():
            nome_categoria = dialogo.obter_nome_categoria()
            self.adicionar_categoria(nome_categoria)

    def adicionar_categoria(self, nome):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM categorias WHERE nome = %s AND usuario_id = %s", 
                           (nome, self.sessao_usuario["id"]))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Erro", "Já existe uma categoria com esse nome.")
                return
            
            cursor.execute("INSERT INTO categorias (nome, usuario_id) VALUES (%s, %s)", 
                           (nome, self.sessao_usuario["id"]))
            conexao.commit()
            QMessageBox.information(self, "Sucesso", f"Categoria '{nome}' adicionada com sucesso.")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar categoria: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def obter_tarefa_marcada(self):
        for coluna in [self.lista_planejamento, self.lista_progresso, self.lista_teste, self.lista_concluido]:
            for linha in range(coluna.widget_lista.count()):
                item = coluna.widget_lista.item(linha)
                widget = coluna.widget_lista.itemWidget(item)
                if widget and widget.checkbox.isChecked():
                    return coluna, item
        return None, None

    def excluir_tarefa(self):
        resposta = QMessageBox.question(self, "Aviso", "Deseja realmente excluir a tarefa?", 
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        coluna, item = self.obter_tarefa_marcada()

        if resposta == QMessageBox.Yes:
            if item is not None:
                texto_tarefa = coluna.widget_lista.itemWidget(item).label_tarefa.text()
                nome = texto_tarefa.split("\n")[0].replace("Tarefa: ", "")

                try:
                    conexao = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="taskzen"
                    )
                    cursor = conexao.cursor()
                    query = "DELETE FROM tarefas WHERE nome = %s AND projeto_id = %s AND usuario_id = %s"
                    cursor.execute(query, (nome, self.projeto.id, self.sessao_usuario["id"]))
                    conexao.commit()
                    QMessageBox.information(self, "Sucesso", f"Tarefa '{nome}' excluída com sucesso.")
                    coluna.widget_lista.takeItem(coluna.widget_lista.row(item))

                except mysql.connector.Error as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao excluir a tarefa: {e}")
                
                finally:
                    if conexao.is_connected():
                        cursor.close()
                        conexao.close()
            else:
                QMessageBox.warning(self, "Aviso", "Nenhuma tarefa foi selecionada.")

    def editar_tarefa(self):
        coluna, item = self.obter_tarefa_marcada()
        if item:
            texto_tarefa_antigo = coluna.widget_lista.itemWidget(item).label_tarefa.text()
            nome_antigo = texto_tarefa_antigo.split("\n")[0].replace("Tarefa: ", "")
            
            try:
                conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="taskzen"
                )
                cursor = conexao.cursor(dictionary=True)
                cursor.execute("SELECT nome, categoria, prioridade, descricao FROM tarefas WHERE nome = %s AND projeto_id = %s AND usuario_id = %s",
                               (nome_antigo, self.projeto.id, self.sessao_usuario["id"]))
                tarefa = cursor.fetchone()
                cursor.close()
                conexao.close()
                
                if tarefa:
                    dialogo = Dialogo_Adicionar_Tarefa(self, editar_tarefa=True, 
                                                     nome=tarefa["nome"], 
                                                     categoria=tarefa["categoria"], 
                                                     prioridade=tarefa["prioridade"], 
                                                     descricao=tarefa["descricao"])
                    if dialogo.exec():
                        nome, categoria, prioridade, descricao = dialogo.obter_dados_tarefa()
                        if nome != nome_antigo:
                            conexao = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="",
                                database="taskzen"
                            )
                            cursor = conexao.cursor()
                            cursor.execute("SELECT COUNT(*) FROM tarefas WHERE nome = %s AND projeto_id = %s AND usuario_id = %s", 
                                           (nome, self.projeto.id, self.sessao_usuario["id"]))
                            if cursor.fetchone()[0] > 0:
                                QMessageBox.warning(self, "Erro", "Já existe uma tarefa com esse nome neste projeto.")
                                cursor.close()
                                conexao.close()
                                return
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
                            UPDATE tarefas SET nome = %s, categoria = %s, prioridade = %s, descricao = %s, coluna = %s
                            WHERE nome = %s AND projeto_id = %s AND usuario_id = %s
                        """, (nome, categoria, prioridade, descricao, coluna.findChild(QLabel).text(), nome_antigo, self.projeto.id, self.sessao_usuario["id"]))
                        conexao.commit()
                        cursor.close()
                        conexao.close()
                        
                        widget = coluna.widget_lista.itemWidget(item)
                        widget.label_tarefa.setText(f"Tarefa: {nome}\nCategoria: {categoria}\nPrioridade: {prioridade}")
            except mysql.connector.Error as e:
                QMessageBox.critical(self, "Erro", f"Erro ao editar tarefa: {e}")
        else:
            QMessageBox.warning(self, "Aviso", "Marque uma tarefa para editar.")

    def mostrar_detalhes_tarefa(self):
        coluna, item = self.obter_tarefa_marcada()
        if item:
            nome_coluna = coluna.findChild(QLabel).text()
            texto_tarefa = coluna.widget_lista.itemWidget(item).label_tarefa.text()
            partes = texto_tarefa.split("\n")
            nome = partes[0]
            categoria = partes[1]
            prioridade = partes[2]
            nome_tarefa = nome.replace("Tarefa: ", "")
            try:
                conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="taskzen"
                )
                cursor = conexao.cursor(dictionary=True)
                cursor.execute("SELECT descricao FROM tarefas WHERE nome = %s AND projeto_id = %s AND usuario_id = %s", 
                               (nome_tarefa, self.projeto.id, self.sessao_usuario["id"]))
                descricao = cursor.fetchone()["descricao"]
                cursor.close()
                conexao.close()
                
                dialogo_detalhes = QDialog(self)
                dialogo_detalhes.setWindowTitle("Detalhes da Tarefa")
                dialogo_detalhes.setMinimumSize(300, 200)
                layout = QVBoxLayout()
                
                label_detalhes = QLabel(f"<b>Coluna:</b> {nome_coluna}<br>"
                                       f"<b>{nome}</b><br>"
                                       f"<b>Categoria:</b> {categoria.split(': ')[1]}<br>"
                                       f"<b>Prioridade:</b> {prioridade.split(': ')[1]}<br>"
                                       f"<b>Descrição:</b> {descricao}")
                label_detalhes.setWordWrap(True)
                layout.addWidget(label_detalhes)
                
                botao_fechar = QPushButton("Fechar")
                botao_fechar.clicked.connect(dialogo_detalhes.accept)
                layout.addWidget(botao_fechar)
                
                dialogo_detalhes.setLayout(layout)
                dialogo_detalhes.setStyleSheet("""
                    QDialog { background-color: #FEF8E8; color: #22354B; }
                    QLabel { padding: 10px; }
                    QPushButton { background-color: #22354B; color: #FEF8E8; padding: 6px; border: 1px solid #22354B; border-radius: 3px; }
                    QPushButton:hover { background-color: #D9A05B; }
                """)
                dialogo_detalhes.exec()
            except mysql.connector.Error as e:
                QMessageBox.critical(self, "Erro", f"Erro ao mostrar detalhes: {e}")
        else:
            QMessageBox.warning(self, "Aviso", "Marque uma tarefa para ver detalhes.")

    def adicionar_tarefa(self, nome, categoria, prioridade, descricao):
        nome = nome[:25]
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM tarefas WHERE nome = %s AND projeto_id = %s AND usuario_id = %s", 
                           (nome, self.projeto.id, self.sessao_usuario["id"]))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Erro", "Já existe uma tarefa com esse nome neste projeto.")
                return
            
            cursor.execute("""
                INSERT INTO tarefas (projeto_id, usuario_id, nome, categoria, prioridade, descricao, coluna)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (self.projeto.id, self.sessao_usuario["id"], nome, categoria, prioridade, descricao, "Em Planejamento"))
            conexao.commit()
            
            texto_tarefa = f"{nome}\nCategoria: {categoria}\nPrioridade: {prioridade}"
            self.lista_planejamento.widget_lista.adicionar_item_tarefa(texto_tarefa)
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar tarefa: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

if __name__ == "__main__":
    app = QApplication([])
    projeto = Projeto(1, "Projeto Teste", "2023-01-01", "2023-12-31")
    sessao_usuario = {"id": 1}
    window = Gerenciador_Tarefas(projeto, sessao_usuario)
    window.show()
    app.exec()