from abc import abstractmethod

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMouseEvent, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from res import resources


class CardView(QWidget):
    HEIGHT_SIZE = 284
    WIDTH_SIZE = 201

    _parent = None
    on_click = None

    def __init__(self, parent, on_click):
        super(CardView, self).__init__(parent)
        self._parent = parent
        self.on_click = on_click
        self.__init_background()
        self._init_foreground()
        self.show()

    def __init_background(self):
        self._background = QLabel("", self)
        self._background.move(0, 0)
        self._background.resize(self.WIDTH_SIZE, self.HEIGHT_SIZE)
        self._background.setPixmap(QPixmap(resources.img_card_view_bg))
        self.setFixedSize(self.WIDTH_SIZE, self.HEIGHT_SIZE)

    def sizeHint(self) -> QSize:
        return QSize(self.WIDTH_SIZE, self.HEIGHT_SIZE)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.on_click()

    @abstractmethod
    def _init_foreground(self):
        raise NotImplementedError("This method must be implemented")
