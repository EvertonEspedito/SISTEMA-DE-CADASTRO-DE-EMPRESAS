from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro de Empresas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)


if __name__ == "__main__":# se o arquivo for executado diretamente
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())