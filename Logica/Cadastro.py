# -*- coding: utf-8 -*-
import re
import random
import mysql.connector
from PySide6.QtWidgets import QMainWindow, QMessageBox
from View.ui_Cadastro import Ui_Cadastro

class Cadastro(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self)

        self.ui.Cadastrar.clicked.connect(self.cadastrar_usuario)
        self.ui.Voltar.clicked.connect(self.voltar)

    def voltar(self):
        if self.main_window:
            self.main_window.show()
            self.close()
        else:
            from Logica.Tela_Inicio import TelaInicio
            self.tela_inicio = TelaInicio()
            self.tela_inicio.show()
            self.close()

    def validar_email(self, email):
        """Valida o formato do email."""
        padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(padrao_email, email) is not None

    def cadastrar_usuario(self):
        usuario = self.ui.user_input.text().strip()
        email = self.ui.email_input.text().strip()
        senha = self.ui.senha_input.text().strip()
        senha2 = self.ui.senha2_input.text().strip()

        # Verifica se todos os campos foram preenchidos
        if not usuario or not email or not senha or not senha2:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos.")
            return

        # Verifica se as senhas coincidem
        if senha != senha2:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem.")
            return

        # Valida o e-mail
        if not self.validar_email(email):
            QMessageBox.warning(self, "Erro", "Email inválido.")
            return

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor()

            # Gerar chave aleatória
            caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
            chave = ''.join(random.choice(caracteres) for _ in range(32))

            # Criptografar a senha
            seed_user = sum(ord(c) for c in chave)

            def gerar(seed, indice):
                random.seed(seed + indice)
                return random.randint(1, 255)

            senha_criptografada = ''.join(hex(gerar(seed_user, ord(c)))[2:] for c in senha)

            # Inserir usuário no banco de dados
            cursor.execute("INSERT INTO usuarios (usuario, email, senha, chave) VALUES (%s, %s, %s, %s)",
                           (usuario, email, senha_criptografada, chave))
            conexao.commit()

            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")

            # Limpar campos
            self.ui.user_input.clear()
            self.ui.email_input.clear()
            self.ui.senha_input.clear()
            self.ui.senha2_input.clear()

            # Voltar para a tela inicial
            if self.main_window:
                self.main_window.show()
            else:
                from Logica.Tela_Inicio import TelaInicio
                self.tela_inicio = TelaInicio()
                self.tela_inicio.show()
                
            self.close()

        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar usuário: {erro}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
