from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel

from data.soldier import Soldier
from res import resources
from ui.widgets.card.card_view import CardView


class SoldierCard(CardView):
    soldier: Soldier

    def __init__(self, parent, soldier: Soldier, on_click):
        self.soldier = soldier
        super().__init__(parent, None)
        self.on_click = lambda: on_click(self.soldier)

    def _init_foreground(self):
        self.army_title = QLabel("육군", self)
        self.army_title.setAlignment(Qt.AlignHCenter)
        self.army_title.setFont(QFont('a몬스터', 36))
        self.army_title.move(0, 16)
        self.army_title.resize(self.WIDTH_SIZE, 100)
        self.army_title.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: {}'
                                      .format(resources.color_soldier_card_title))

        self.army_picture = QLabel(self)
        self.army_picture.setPixmap(QPixmap(resources.img_army_picture))
        self.army_picture.setAlignment(Qt.AlignHCenter)
        self.army_picture.resize(self.WIDTH_SIZE, 120)
        self.army_picture.move(0, 80)
        self.army_picture.setStyleSheet('background-color: rgba(0, 0, 0, 0)')

        self.left_date_label = QLabel("D-" + self.__calc_left_day(), self)
        self.left_date_label.setAlignment(Qt.AlignHCenter)
        self.left_date_label.setFont(QFont('a어린왕자M', 32))
        self.left_date_label.move(0, 204)
        self.left_date_label.resize(self.WIDTH_SIZE, 100)
        self.left_date_label.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: {}'
                                           .format(resources.color_soldier_card_text))

        self.soldier_name_label = QLabel("훈련병 " + self.soldier.name, self)
        self.soldier_name_label.setAlignment(Qt.AlignHCenter)
        self.soldier_name_label.setFont(QFont('a어린왕자M', 20))
        self.soldier_name_label.move(0, 244)
        self.soldier_name_label.resize(self.WIDTH_SIZE, 100)
        self.soldier_name_label.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: {}'
                                              .format(resources.color_soldier_card_text))

    def __calc_left_day(self):
        return str((self.soldier.complete_date - datetime.today()).days)

    def on_click(self):
        pass
