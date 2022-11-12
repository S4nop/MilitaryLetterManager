import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton

from res import resources
from ui.widgets.shadow_rect_widget import ShadowRectFrame
from ui.widgets.styled_button import StyledButton
from utils.utils import move_window_to_center


class NewsTypeSelectDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()
    
    def __init_ui(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 400, 580)
        self.setStyleSheet('background-color: {};'.format(resources.color_gray_bg))
        move_window_to_center(self)

        self.__init_first_frame()
        self.__init_second_frame()
        self.__init_third_frame()

        self.close_button = StyledButton(self)
        self.close_button.setText("Close")
        self.close_button.resize(384, 50)
        self.close_button.move(8, 520)
        self.close_button.mouseReleaseEvent = lambda _: self.on_click_close()

    def __init_first_frame(self):
        self.bg_top = ShadowRectFrame(self)
        self.bg_top.resize(390, 160)
        self.bg_top.move(5, 8)

        self.ArmyType = QLabel("육군", self.bg_top)
        self.ArmyType.setFont(QFont('a몬스터', 32))
        self.ArmyType.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.ArmyType.move(30, 60)
        self.ArmyType.setAlignment(Qt.AlignCenter)

        self.SoldierImage = QLabel(self.bg_top)
        self.SoldierImage.setPixmap(QPixmap(resources.img_army_picture))
        self.SoldierImage.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        #self.SoldierImage.setPixmap(QPixmap("army_picture.png"))
        self.SoldierImage.resize(150, 150)
        self.SoldierImage.move(120, 10)
        self.SoldierImage.setAlignment(Qt.AlignCenter)

        self.Dday = QLabel("D-3", self.bg_top)
        self.Dday.setAlignment(Qt.AlignCenter)
        self.Dday.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: {};'.format(resources.color_login_activity_text))
        self.Dday.setFont(QFont('a어린왕자M', 36))
        self.Dday.resize(100, 50)
        self.Dday.move(272, 42)

        self.SoldierName = QLabel("훈련병 우지은", self.bg_top)
        self.SoldierName.setAlignment(Qt.AlignCenter)
        self.SoldierName.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: {};'.format(resources.color_login_activity_text))
        self.SoldierName.setFont(QFont('a어린왕자M', 16, weight=QFont.Bold))
        self.SoldierName.resize(120, 50)
        self.SoldierName.move(264, 80)

    def __init_second_frame(self):
        self.bg_mid = ShadowRectFrame(self)
        self.bg_mid.resize(390, 100)
        self.bg_mid.move(5, 172)

        self.LastLetter = QLabel("마지막으로 전송한 날짜", self.bg_mid)
        self.LastLetter.setAlignment(Qt.AlignLeft)
        self.LastLetter.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.LastLetter.setFont(QFont('a꾸러기', 16))
        self.LastLetter.resize(200, 40)
        self.LastLetter.move(20, 20)

        self.LLDate = QLabel("2022-11-03", self.bg_mid)
        self.LLDate.setAlignment(Qt.AlignRight)
        self.LLDate.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.LLDate.setFont(QFont('Roboto', 12))
        self.LLDate.resize(120, 40)
        self.LLDate.move(250, 20)

        self.SentLetter = QLabel("전송된 인편 갯수", self.bg_mid)
        self.SentLetter.setAlignment(Qt.AlignLeft)
        self.SentLetter.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.SentLetter.setFont(QFont('a꾸러기', 16))
        self.SentLetter.resize(200, 40)
        self.SentLetter.move(20, 60)

        self.SLNum = QLabel("15개", self.bg_mid)
        self.SLNum.setAlignment(Qt.AlignRight)
        self.SLNum.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.SLNum.setFont(QFont('Roboto', 12))
        self.SLNum.resize(120, 40)
        self.SLNum.move(250, 60)

    def __init_third_frame(self):
        self.bg_bottom = ShadowRectFrame(self)
        self.bg_bottom.resize(390, 240)
        self.bg_bottom.move(5, 276)

        self.NewsCate = QLabel("전송할 뉴스 카테고리", self.bg_bottom)
        self.NewsCate.setAlignment(Qt.AlignLeft)
        self.NewsCate.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.NewsCate.setFont(QFont('a꾸러기', 16))
        self.NewsCate.resize(200, 40)
        self.NewsCate.move(20, 20)

        self.Poli = QCheckBox("정치", self.bg_bottom)
        self.Poli.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.Econ = QCheckBox("경제", self.bg_bottom)
        self.Econ.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.Soci = QCheckBox("사회", self.bg_bottom)
        self.Soci.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.Cult = QCheckBox("생활/문화", self.bg_bottom)
        self.Cult.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.ITSc = QCheckBox("IT/과학", self.bg_bottom)
        self.ITSc.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.Spor = QCheckBox("스포츠", self.bg_bottom)
        self.Spor.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')

        layout_bottom = QGridLayout(self.bg_bottom)
        layout_bottom.addWidget(self.Poli, 1, 0)
        layout_bottom.addWidget(self.Econ, 1, 1)
        layout_bottom.addWidget(self.Soci, 2, 0)
        layout_bottom.addWidget(self.Cult, 2, 1)
        layout_bottom.addWidget(self.ITSc, 3, 0)
        layout_bottom.addWidget(self.Spor, 3, 1)
        layout_bottom.setAlignment(Qt.AlignTop)
        layout_bottom.setContentsMargins(20, 60, 20, 20)
        layout_bottom.setSpacing(12)

    def on_click_close(self):
        self.close()
