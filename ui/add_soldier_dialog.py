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
from ui.widgets.styled_text_field import StyledLineEdit
from utils.utils import move_window_to_center


class AddSoldierDialog(QMainWindow):
    DIALOG_WIDTH = 400
    DIALOG_HEIGHT = 250

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Add Soldier')
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
        move_window_to_center(self)
        self.__init_background()
        self.__init_elements()

    def __init_background(self):
        self.bg_left = QLabel(self)
        self.bg_left.setAlignment(Qt.AlignHCenter)
        self.bg_left.resize(self.DIALOG_WIDTH / 2, self.DIALOG_HEIGHT)
        self.bg_left.move(0, 0)
        self.bg_left.setStyleSheet('background-color: {}'.format(resources.color_white))

        self.bg_right = QLabel(self)
        self.bg_right.setAlignment(Qt.AlignHCenter)
        self.bg_left.resize(self.DIALOG_WIDTH / 2, self.DIALOG_HEIGHT)
        self.bg_right.move(self.DIALOG_WIDTH / 2, 0)
        self.bg_right.setStyleSheet('background-color: {}'.format(resources.color_gray_bg))

    def __init_elements(self):
        self.ArmyType = QLabel("육군", self)
        self.ArmyType.setFont(QFont('a몬스터', 40))
        self.ArmyType.resize(self.DIALOG_WIDTH / 2, 100)
        self.ArmyType.move(0, 10)
        self.ArmyType.setAlignment(Qt.AlignCenter)

        self.SoldierImage = QLabel(self)
        self.SoldierImage.setPixmap(QPixmap(resources.img_army_picture))
        self.SoldierImage.resize(self.DIALOG_WIDTH / 2, 170)
        self.SoldierImage.move(0, 80)
        self.SoldierImage.setAlignment(Qt.AlignCenter)

        self.NameInput = StyledLineEdit(self)
        self.NameInput.resize(180, 32)
        self.NameInput.move(int(self.DIALOG_WIDTH / 2) + 10, 34)
        self.NameInput.setPlaceholderText("성명")

        self.EnlistDayInput = StyledLineEdit(self)
        self.EnlistDayInput.resize(180, 32)
        self.EnlistDayInput.move(int(self.DIALOG_WIDTH / 2) + 10, 84)
        self.EnlistDayInput.setPlaceholderText("입영일(YYYY-MM-DD)")

        self.BDayInput = StyledLineEdit(self)
        self.BDayInput.resize(180, 32)
        self.BDayInput.move(int(self.DIALOG_WIDTH / 2) + 10, 134)
        self.BDayInput.setPlaceholderText("생일(YYYY-MM-DD)")

        self.add_btn = StyledButton(self)
        self.add_btn.setText('Add')
        self.add_btn.resize(180, 40)
        self.add_btn.move(int(self.DIALOG_WIDTH / 2) + 10, 194)
        self.add_btn.set_font_size(12)
        self.add_btn.set_on_click(self.add)

        self.close_button = QLabel(self)
        self.close_button.setPixmap(QPixmap(resources.img_close))
        self.close_button.setScaledContents(True)
        self.close_button.resize(30, 30)
        self.close_button.move(370, 0)
        self.close_button.mouseReleaseEvent = self.close


    def add(self):
        Name = self.NameInput.text()
        EnlistDay = self.EnlistDayInput.text()
        BDay = self.BDayInput.text()
        
        self.close()
