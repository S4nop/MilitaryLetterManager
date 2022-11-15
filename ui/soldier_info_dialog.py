from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont

from data.news_choice import NewsChoice
from data.soldier_letter_info import SoldierLetterInfo
from res import resources
from ui.widgets.shadow_rect_widget import ShadowRectFrame
from ui.widgets.styled_button import StyledButton
from utils.utils import move_window_to_center


class SoldierInfoDialog(QDialog):
    DIALOG_WIDTH = 400
    DIALOG_HEIGHT = 580

    name: str
    left_day: str
    letter_info: SoldierLetterInfo

    def __init__(self, parent, name, left_day, letter_info, on_closed):
        super().__init__(parent, Qt.WindowFlags(Qt.FramelessWindowHint))
        self.on_closed = on_closed
        self.name = name
        self.left_day = str(left_day)
        self.letter_info = letter_info
        self.__init_ui()
        self.show()

    def __init_ui(self):
        self.setGeometry(0, 0, self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
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

        self.army_title = QLabel("육군", self.bg_top)
        self.army_title.setFont(QFont('a몬스터', 32))
        self.army_title.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.army_title.move(30, 60)
        self.army_title.setAlignment(Qt.AlignCenter)

        self.soldier_image = QLabel(self.bg_top)
        self.soldier_image.setPixmap(QPixmap(resources.img_army_picture))
        self.soldier_image.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.soldier_image.resize(150, 150)
        self.soldier_image.move(120, 10)
        self.soldier_image.setAlignment(Qt.AlignCenter)

        self.d_day = QLabel("D-" + self.left_day, self.bg_top)
        self.d_day.setAlignment(Qt.AlignCenter)
        self.d_day.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: {};'
                                 .format(resources.color_login_activity_text))
        self.d_day.setFont(QFont('a어린왕자M', 36))
        self.d_day.resize(100, 50)
        self.d_day.move(272, 42)

        self.soldier_name = QLabel("훈련병 " + self.name, self.bg_top)
        self.soldier_name.setAlignment(Qt.AlignCenter)
        self.soldier_name.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: {};'
                                        .format(resources.color_login_activity_text))
        self.soldier_name.setFont(QFont('a어린왕자M', 16, weight=QFont.Bold))
        self.soldier_name.resize(120, 50)
        self.soldier_name.move(264, 80)

    def __init_second_frame(self):
        self.bg_mid = ShadowRectFrame(self)
        self.bg_mid.resize(390, 100)
        self.bg_mid.move(5, 172)

        self.last_send_date_title = QLabel("마지막으로 전송한 날짜", self.bg_mid)
        self.last_send_date_title.setAlignment(Qt.AlignLeft)
        self.last_send_date_title.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.last_send_date_title.setFont(QFont('a꾸러기', 16))
        self.last_send_date_title.resize(200, 40)
        self.last_send_date_title.move(20, 20)

        self.last_send_date = QLabel(self.letter_info.last_sent_date, self.bg_mid)
        self.last_send_date.setAlignment(Qt.AlignRight)
        self.last_send_date.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.last_send_date.setFont(QFont('Roboto', 12))
        self.last_send_date.resize(120, 40)
        self.last_send_date.move(250, 20)

        self.sent_letter_count_title = QLabel("전송된 인편 갯수", self.bg_mid)
        self.sent_letter_count_title.setAlignment(Qt.AlignLeft)
        self.sent_letter_count_title.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.sent_letter_count_title.setFont(QFont('a꾸러기', 16))
        self.sent_letter_count_title.resize(200, 40)
        self.sent_letter_count_title.move(20, 60)

        self.sent_letter_count = QLabel(str(self.letter_info.letter_count), self.bg_mid)
        self.sent_letter_count.setAlignment(Qt.AlignRight)
        self.sent_letter_count.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.sent_letter_count.setFont(QFont('Roboto', 12))
        self.sent_letter_count.resize(120, 40)
        self.sent_letter_count.move(250, 60)

    def __init_third_frame(self):
        letter_category_choice = self.letter_info.letter_news_category

        self.bg_bottom = ShadowRectFrame(self)
        self.bg_bottom.resize(390, 240)
        self.bg_bottom.move(5, 276)

        self.news_category_title = QLabel("전송할 뉴스 카테고리", self.bg_bottom)
        self.news_category_title.setAlignment(Qt.AlignLeft)
        self.news_category_title.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.news_category_title.setFont(QFont('a꾸러기', 16))
        self.news_category_title.resize(200, 40)
        self.news_category_title.move(20, 20)

        self.politics = QCheckBox("정치", self.bg_bottom)
        self.politics.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.politics.setChecked(letter_category_choice.get_politic_flag() == 1)
        self.economy = QCheckBox("경제", self.bg_bottom)
        self.economy.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.economy.setChecked(letter_category_choice.get_economy_flag() == 1)
        self.society = QCheckBox("사회", self.bg_bottom)
        self.society.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.society.setChecked(letter_category_choice.get_society_flag() == 1)
        self.culture = QCheckBox("생활/문화", self.bg_bottom)
        self.culture.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.culture.setChecked(letter_category_choice.get_lifeculture_flag() == 1)
        self.it_science = QCheckBox("IT/과학", self.bg_bottom)
        self.it_science.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.it_science.setChecked(letter_category_choice.get_itscience_flag() == 1)
        self.worlds = QCheckBox("세계", self.bg_bottom)
        self.worlds.setStyleSheet('background-color: rgba(0, 0, 0, 0); Color: #3d3d3d;')
        self.worlds.setChecked(letter_category_choice.get_world_flag() == 1)

        layout_bottom = QGridLayout(self.bg_bottom)
        layout_bottom.addWidget(self.politics, 1, 0)
        layout_bottom.addWidget(self.economy, 1, 1)
        layout_bottom.addWidget(self.society, 2, 0)
        layout_bottom.addWidget(self.culture, 2, 1)
        layout_bottom.addWidget(self.it_science, 3, 0)
        layout_bottom.addWidget(self.worlds, 3, 1)
        layout_bottom.setAlignment(Qt.AlignTop)
        layout_bottom.setContentsMargins(20, 60, 20, 20)
        layout_bottom.setSpacing(12)

    def on_click_close(self):
        news_choice = NewsChoice()
        if self.worlds.isChecked():
            news_choice.set_world_flag()
        if self.politics.isChecked():
            news_choice.set_politic_flag()
        if self.economy.isChecked():
            news_choice.set_economy_flag()
        if self.society.isChecked():
            news_choice.set_society_flag()
        if self.culture.isChecked():
            news_choice.set_lifeculture_flag()
        if self.it_science.isChecked():
            news_choice.set_itscience_flag()

        self.on_closed(news_choice)
        self.close()
