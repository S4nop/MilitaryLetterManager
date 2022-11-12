from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QFrame

from res import resources


class ShadowRectFrame(QFrame):
    def __init__(self, parent):
        super(ShadowRectFrame, self).__init__(parent)
        self.show()

    def __draw_bg_as_nine_patch(self):
        painter = QPainter(self)
        bg = QPixmap(resources.img_shadow_rect)
        left_top = bg.copy(0, 0, 10, 10)
        top = bg.copy(10, 0, bg.width() - 20, 10)
        right_top = bg.copy(bg.width() - 10, 0, 10, 10)
        left = bg.copy(0, 10, 10, bg.height() - 20)
        center = bg.copy(10, 10, bg.width() - 20, bg.height() - 20)
        right = bg.copy(bg.width() - 10, 10, 10, bg.height() - 20)
        left_bottom = bg.copy(0, bg.height() - 10, 10, 10)
        bottom = bg.copy(10, bg.height() - 10, bg.width() - 20, 10)
        right_bottom = bg.copy(bg.width() - 10, bg.height() - 10, 10, 10)
        painter.drawPixmap(0, 0, 10, 10, left_top)
        painter.drawPixmap(10, 0, self.width() - 20, 10, top)
        painter.drawPixmap(self.width() - 10, 0, 10, 10, right_top)
        painter.drawPixmap(0, 10, 10, self.height() - 20, left)
        painter.drawPixmap(10, 10, self.width() - 20, self.height() - 20, center)
        painter.drawPixmap(self.width() - 10, 10, 10, self.height() - 20, right)
        painter.drawPixmap(0, self.height() - 10, 10, 10, left_bottom)
        painter.drawPixmap(10, self.height() - 10, self.width() - 20, 10, bottom)
        painter.drawPixmap(self.width() - 10, self.height() - 10, 10, 10, right_bottom)

    def paintEvent(self, event):
        self.__draw_bg_as_nine_patch()
