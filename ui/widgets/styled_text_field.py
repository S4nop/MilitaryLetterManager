from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit

from res import resources


class StyledLineEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.__init_style()

    def __init_style(self):
        self.setStyleSheet('background-color: {}; Color: {}; '
                                    'border-radius: 2px; border: 1px solid {}; padding: 6px;'
                                    .format(resources.color_white,
                                            resources.color_login_activity_text,
                                            resources.color_text_field_border))
        self.setFont(QFont('a어린왕자M', 12))

    def set_font_size(self, size):
        self.setFont(QFont('a어린왕자M', size, weight=QFont.Bold))
