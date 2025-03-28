from PySide6.QtWidgets import QMainWindow
from View.ui_Tela_Inicio import Ui_TelaInicio  # Importa da pasta view
from Logica.Login import Login  # Importa da pasta logico
from Logica.Cadastro import Cadastro  # Importa da pasta logico

class TelaInicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaInicio()
        self.ui.setupUi(self)
        
        # Conectar os botões às funções
        self.ui.Login.clicked.connect(self.open_login)
        self.ui.Login2.clicked.connect(self.open_login)
        self.ui.Cadastrar.clicked.connect(self.open_cadastro)

    def open_login(self):
        self.login_window = Login(self)  # Passa a referência da TelaInicio
        self.login_window.show()  # Apenas exibe a janela
        self.close()

    def open_cadastro(self):
        self.cadastro_window = Cadastro(self)  # Passa a referência da TelaInicio
        self.cadastro_window.show()  # Apenas exibe a janela
        self.close()
    