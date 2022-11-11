import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton

from res import resources

class AddSoldierDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Add Soldier')
        self.setGeometry(300, 300, 600, 300)
        self.__init_background()
        self.__init_elements()

    def __init_background(self):
        self.bg_left = QLabel(self)
        self.bg_left.setAlignment(Qt.AlignHCenter)
        self.bg_left.resize(300, 300)
        self.bg_left.move(0, 0)
        self.bg_left.setStyleSheet('background-color: {}'.format(resources.color_background))
        #self.bg_left.setStyleSheet('background-color: white')

        self.bg_right = QLabel(self)
        self.bg_right.setAlignment(Qt.AlignHCenter)
        self.bg_right.resize(300, 300)
        self.bg_right.move(300, 0)
        self.bg_right.setStyleSheet('background-color: {}'.format(resources.color_primary))
        #self.bg_right.setStyleSheet('background-color: grey')

    def __init_elements(self):
        self.left_widget = QWidget(self)
        self.left_widget.resize(300, 300)
        self.left_widget.move(0, 0)

        self.right_widget = QWidget(self)
        self.right_widget.resize(300, 300)
        self.right_widget.move(300, 0)

        self.ArmyType = QLabel("육군")
        self.ArmyType.setFont(QFont('a몬스터', 56))
        self.ArmyType.setStyleSheet('Color: {}'.format(resources.color_primary))
        #self.ArmyType.setAlignment(Qt.AlignCenter)

        self.SoldierImage = QLabel()
        self.SoldierImage.setPixmap(QPixmap('{}'.format(resources.army_picture)))
        #self.SoldierImage.setPixmap(QPixmap("army_picture.png"))
        self.SoldierImage.setAlignment(Qt.AlignCenter)

        self.NameInput = QLineEdit()
        self.NameInput.setPlaceholderText("성명")
        self.NameInput.setFont(QFont('a꾸러기'))

        self.EnlistDayInput = QLineEdit()
        self.EnlistDayInput.setPlaceholderText("입영일(YYYY-MM-DD)")
        self.EnlistDayInput.setFont(QFont('a꾸러기'))

        self.BDayInput = QLineEdit()
        self.BDayInput.setPlaceholderText("생일(YYYY-MM-DD)")
        self.BDayInput.setFont(QFont('a꾸러기'))

        self.add_btn = QPushButton("Add")
        self.add_btn.setFont(QFont('a꾸러기'))
        self.btn.setStyleSheet('Color: {}'.format(resources.color_primary))
        self.add_btn.clicked.connect(self.add)

        layout_left = QVBoxLayout(self.left_widget)
        layout_left.addWidget(self.ArmyType)
        layout_left.addWidget(self.SoldierImage)
        self.setLayout(layout_left)

        layout_right = QVBoxLayout(self.right_widget)
        layout_right.addWidget(self.NameInput)
        layout_right.addWidget(self.EnlistDayInput)
        layout_right.addWidget(self.BDayInput)
        layout_right.addWidget(self.add_btn)
        self.setLayout(layout_right)

    def add(self):
        Name = self.NameInput.text()
        EnlistDay = self.EnlistDayInput.text()
        BDay = self.BDayInput.text()
        
        self.close()
