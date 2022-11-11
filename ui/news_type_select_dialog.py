import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton

from res import resources

class NewsTypeSelectDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()
    
    def __init_ui(self):
        self.setWindowTitle('News Type Select')
        self.setGeometry(300, 300, 360, 550)
        self.__init_background()
        self.__init_elements()

    def __init_background(self):
        self.bg_back = QLabel(self)
        self.bg_back.setAlignment(Qt.AlignHCenter)
        self.bg_back.resize(360, 570)
        self.bg_back.move(0, 0)
        self.bg_back.setStyleSheet('background-color: {}'.format(resources.color_background))
        #self.bg_back.setStyleSheet('background-color: grey')

        self.bg_top = QLabel(self)
        self.bg_top.setAlignment(Qt.AlignHCenter)
        self.bg_top.resize(350, 150)
        self.bg_top.move(5, 5)
        self.bg_top.setStyleSheet('background-color: {}'.format(resources.color_background))
        #self.bg_top.setStyleSheet('background-color: white')

        self.bg_mid = QLabel(self)
        self.bg_mid.setAlignment(Qt.AlignHCenter)
        self.bg_mid.resize(350, 100)
        self.bg_mid.move(5, 160)
        self.bg_mid.setStyleSheet('background-color: {}'.format(resources.color_background))
        #self.bg_mid.setStyleSheet('background-color: white')

        self.bg_bottom = QLabel(self)
        self.bg_bottom.setAlignment(Qt.AlignHCenter)
        self.bg_bottom.resize(350, 220)
        self.bg_bottom.move(5, 265)
        self.bg_bottom.setStyleSheet('background-color: {}'.format(resources.color_background))
        #self.bg_bottom.setStyleSheet('background-color: white')

    def __init_elements(self):
        self.topl_widget = QWidget(self)
        self.topl_widget.resize(230, 150)
        self.topl_widget.move(5, 5)

        self.topr_widget = QWidget(self)
        self.topr_widget.resize(120, 150)
        self.topr_widget.move(235, 5)

        self.midl_widget = QWidget(self)
        self.midl_widget.resize(230, 100)
        self.midl_widget.move(5, 160)

        self.midr_widget = QWidget(self)
        self.midr_widget.resize(120, 100)
        self.midr_widget.move(235, 160)
        
        self.bottom_widget = QWidget(self)
        self.bottom_widget.resize(350, 120)
        self.bottom_widget.move(5, 265)

        self.btn_widget = QWidget(self)
        self.btn_widget.resize(350, 50)
        self.btn_widget.move(5, 490)

        self.ArmyType = QLabel("육군")
        self.ArmyType.setFont(QFont('a몬스터', 56))
        self.ArmyType.setStyleSheet('Color: {}'.format(resources.color_primary))
        self.ArmyType.setAlignment(Qt.AlignCenter)

        self.SoldierImage = QLabel()
        self.SoldierImage.setPixmap(QPixmap('{}'.format(resources.army_picture)))
        #self.SoldierImage.setPixmap(QPixmap("army_picture.png"))
        self.SoldierImage.resize(60, 60)
        self.SoldierImage.setAlignment(Qt.AlignCenter)
        
        self.Dday = QLabel("D - 3")
        self.SoldierName = QLabel("훈련병 우지은")

        self.LastLetter = QLabel("마지막으로 전송한 날짜")
        self.LLDate = QLabel("2022-11-03")

        self.SentLetter = QLabel("전송된 인편 갯수")
        self.SLNum = QLabel("15개")

        self.NewsCate = QLabel("전송할 뉴스 카테고리")
        self.Poli = QCheckBox("정치")
        self.Econ = QCheckBox("경제")
        self.Soci = QCheckBox("사회")
        self.Cult = QCheckBox("생활/문화")
        self.ITSc = QCheckBox("IT/과학")
        self.Spor = QCheckBox("스포츠")

        self.close_btn = QPushButton("Close")
        self.close_btn.resize(350, 50)
        self.close_btn.setFont(QFont('a꾸러기'))
        self.close_btn.setStyleSheet('Color: {}'.format(resources.color_primary))
        self.close_btn.clicked.connect(self.close)

        layout_topl = QHBoxLayout(self.topl_widget)
        layout_topl.addWidget(self.ArmyType)
        layout_topl.addWidget(self.SoldierImage)
        self.setLayout(layout_topl)

        layout_topr = QVBoxLayout(self.topr_widget)
        layout_topr.addWidget(self.Dday)
        layout_topr.addWidget(self.SoldierName)
        self.setLayout(layout_topr)

        layout_midl = QVBoxLayout(self.midl_widget)
        layout_midl.addWidget(self.LastLetter)
        layout_midl.addWidget(self.SentLetter)
        self.setLayout(layout_midl)

        layout_midr = QVBoxLayout(self.midr_widget)
        layout_midr.addWidget(self.LLDate)
        layout_midr.addWidget(self.SLNum)
        self.setLayout(layout_midr)

        layout_bottom = QGridLayout(self.bottom_widget)
        layout_bottom.addWidget(self.NewsCate, 0, 0)
        layout_bottom.addWidget(self.Poli, 1, 0)
        layout_bottom.addWidget(self.Econ, 1, 1)
        layout_bottom.addWidget(self.Soci, 2, 0)
        layout_bottom.addWidget(self.Cult, 2, 1)
        layout_bottom.addWidget(self.ITSc, 3, 0)
        layout_bottom.addWidget(self.Spor, 3, 1)
        self.setLayout(layout_bottom)

        layout_btn = QHBoxLayout(self.btn_widget)
        layout_btn.addWidget(self.close_btn)
        self.setLayout(layout_btn)
