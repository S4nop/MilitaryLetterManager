import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton

from res import resources
from ui.widgets.styled_button import StyledButton
from utils.utils import move_window_to_center


class LoginActivity(QMainWindow):
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Login')
        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet('background-color: {};'.format(resources.color_gray_bg))
        move_window_to_center(self)

        self.title = QLabel("THE CAMP", self)
        self.title.setFont(QFont('a몬스터', 40))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.resize(self.WINDOW_WIDTH, 50)
        self.title.move(0, 50)
        self.title.setStyleSheet('Color: {}'.format(resources.color_primary))

        self.id_input = QLineEdit("", self)
        self.id_input.resize(300, 40)
        self.id_input.move(50, 140)
        self.id_input.setStyleSheet('background-color: {}; border-radius: 4px; border: 1px solid {}'
                                    .format(resources.color_white, resources.color_text_field_border))

        self.pw_input = QLineEdit("", self)
        self.pw_input.resize(300, 40)
        self.pw_input.move(50, 190)
        self.pw_input.setStyleSheet('background-color: {}; border-radius: 4px; border: 1px solid {}'
                                    .format(resources.color_white, resources.color_text_field_border))

        self.login_button = StyledButton(self)
        self.login_button.set_text('Login')
        self.login_button.set_on_click(self.login)
        self.login_button.resize(300, 44)
        self.login_button.move(50, 250)

    def login(self):
        ID = self.id_input.text()
        PW = self.pw_input.text()
        self.close()
