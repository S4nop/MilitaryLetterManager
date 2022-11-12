from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from ui.widgets.card.card_view import CardView


class AddActionCard(CardView):
    def _init_foreground(self):
        self.add_img = QLabel(self)
        self.add_img.setPixmap(QPixmap('./res/img/add.png'))
        self.add_img.setAlignment(Qt.AlignHCenter)
        self.add_img.resize(self.WIDTH_SIZE, 120)
        self.add_img.setStyleSheet('background-color: rgba(0, 0, 0, 0)')
        self.add_img.move(0, 80)

    def on_click(self):
        pass
