# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QMessageBox
from View.ui_Login import Ui_Login
import mysql.connector
from Logica.Tela_Tarefas import Tela_Tarefas
import random

class Login(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.Btn_voltar.clicked.connect(self.voltar_login)
        self.ui.Btn_entrar.clicked.connect(self.fazer_login)

    def voltar_login(self):
        if self.main_window:
            self.main_window.show()
            self.close()
        else:
            from Logica.Tela_Inicio import TelaInicio
            self.tela_inicio = TelaInicio()
            self.tela_inicio.show()
            self.close()

    def fazer_login(self):
        email = self.ui.lineEdit_usuario.text().strip()
        senha = self.ui.lineEdit_senha.text().strip()

        if not email or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taskzen"
            )
            cursor = conexao.cursor(dictionary=True)

            cursor.execute("SELECT id, senha, chave FROM usuarios WHERE email = %s", (email,))
            usuario_encontrado = cursor.fetchone()

            if usuario_encontrado:
                seed_user = 0
                for i in range(0, len(usuario_encontrado["chave"])):
                    seed_user += ord(usuario_encontrado["chave"][i])
                
                def gerar(seed, indice):
                    random.seed(seed + indice)
                    return random.randint(1, 255)
                
                temp1 = ''
                for i in range(0, len(senha)):
                    temp = hex(gerar(seed_user, ord(senha[i])))[2:]
                    temp1 += temp

                if temp1 == usuario_encontrado["senha"]:
                    QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
                    self.user_session = {"id": usuario_encontrado["id"]}
                    self.close()
                    # Adicionar try-except para capturar erros ao abrir Tela_Tarefas
                    try:
                        self.tarefa_window = Tela_Tarefas(self.user_session)
                        self.tarefa_window.show()
                    except Exception as e:
                        QMessageBox.critical(self, "Erro", f"Erro ao abrir Tela_Tarefas: {str(e)}")
                        # Voltar para a tela inicial em caso de erro
                        if self.main_window:
                            self.main_window.show()
                        else:
                            from Logica.Tela_Inicio import TelaInicio
                            self.tela_inicio = TelaInicio()
                            self.tela_inicio.show()
                else:
                    QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")
            else:
                QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

        except mysql.connector.Error as erro:
            QMessageBox.critical(self, "Erro", f"Erro ao conectar ao banco: {erro}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()