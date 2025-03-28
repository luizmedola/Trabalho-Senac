import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt  # Importa o Qt para usar AA_UseHighDpiPixmaps
from Logica.Tela_Inicio import TelaInicio  # Importa da pasta logico

def main():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)  # Melhora a qualidade de imagens em telas de alta DPI
    
    # Inicializa e exibe a tela inicial
    window = TelaInicio()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()