from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton


class LoginActivity(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Login')
        self.setGeometry(300, 300, 300, 200)

        self.login_button = QPushButton('Login', self)
        self.login_button.move(100, 100)
        self.login_button.clicked.connect(self.login)

    def login(self):
        self.close()