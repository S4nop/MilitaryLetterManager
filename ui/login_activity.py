import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton

from res import resources

class LoginActivity(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Login')
        self.setGeometry(300, 300, 300, 200)

        self.title = QLabel("THE CAMP", self)
        self.title.setFont(QFont('a몬스터', 20))
        self.title.move(100, 0)
        self.title.setStyleSheet('Color: {}'.format(resources.color_primary))

        self.id_input = QLineEdit(" ", self)
        self.id_input.move(100, 50)

        self.pw_input = QLineEdit(" ", self)
        self.pw_input.move(100, 100)

        self.login_button = QPushButton('Login', self)
        self.login_button.move(100, 150)
        self.login_button.setStyleSheet('Color: {}'.format(resources.color_primary))
        self.login_button.clicked.connect(self.login)

    def login(self):
        ID = self.id_input.text()
        PW = self.pw_input.text()
        self.close()
