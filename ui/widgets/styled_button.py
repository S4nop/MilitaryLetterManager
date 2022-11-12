from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from res import resources


class StyledButton(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.__init_style()

    def set_text(self, text):
        self.setText(text)

    def set_font_size(self, size):
        self.setFont(QFont('Roboto', size, weight=QFont.Bold))

    def set_on_click(self, on_click):
        self.mousePressEvent = lambda _: on_click()

    def __init_style(self):
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Roboto', 16, weight=QFont.Bold))
        self.setStyleSheet('background-color: {}; Color: {}; border-radius: 4px;'
                           .format(resources.color_primary, resources.color_white))
