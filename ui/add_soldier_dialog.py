import re

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont

from res import resources
from client.main_client import MainClient
from ui.widgets.styled_button import StyledButton
from ui.widgets.styled_text_field import StyledLineEdit
from utils.utils import move_window_to_center
from manager.thecamp_session_manager import TheCampSessionManager


class AddSoldierDialog(QDialog):
    DIALOG_WIDTH = 400
    DIALOG_HEIGHT = 250

    belongings_map = {'선택':'', '육군훈련소-논산': '20020191700', '육군3사관학교': '20020920000', '1사단-파주': '20121290100',
                      '2사단': '20121490100', '3사단-철원': '20121590100', '5사단-연천': '20121690200', '6사단-철원': '20121590200',
                      '7사단-화천': '20121390100', '9사단-고양': '20121290200', '11사단': '20121790300', '12사단-인제': '20121490200',
                      '15사단-화천': '20121390200', '17사단': '20121190100', '20사단': '20121790400', '21사단-양구': '20121490300',
                      '22사단': '20121890100', '23사단': '20121890200', '25사단-양주': '20121290300', '27사단-화천': '20121390300',
                      '28사단-파주': '20121690100', '30사단': '20121290400', '31사단-광주': '20220280100',
                      '32사단-세종': '20220280200', '35사단-임실': '20220280300', '36사단-원주': '20120180100',
                      '37사단-증평': '20220280400', '39사단-함안': '20220280500', '50사단-대구': '20220280600',
                      '51사단-화성': '20121190200', '53사단-부산': '20220280700', '55사단-용인': '20120180200'}

    def __init__(self, parent, on_closed):
        super().__init__(parent, Qt.WindowFlags(Qt.FramelessWindowHint))
        self.__init_ui()
        self.on_closed = on_closed
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Add Soldier')
        self.setGeometry(0, 0, self.DIALOG_WIDTH, self.DIALOG_HEIGHT)
        move_window_to_center(self)
        self.__init_background()
        self.__init_elements()

    def __init_background(self):
        self.bg_left = QLabel(self)
        self.bg_left.setAlignment(Qt.AlignHCenter)
        self.bg_left.resize(self.DIALOG_WIDTH / 2, self.DIALOG_HEIGHT)
        self.bg_left.move(0, 0)
        self.bg_left.setStyleSheet('background-color: {}'.format(resources.color_white))

        self.bg_right = QLabel(self)
        self.bg_right.setAlignment(Qt.AlignHCenter)
        self.bg_left.resize(self.DIALOG_WIDTH / 2, self.DIALOG_HEIGHT)
        self.bg_right.move(self.DIALOG_WIDTH / 2, 0)
        self.bg_right.setStyleSheet('background-color: {}'.format(resources.color_gray_bg))

    def __init_elements(self):
        self.army_title = QLabel("육군", self)
        self.army_title.setFont(QFont('a몬스터', 40))
        self.army_title.resize(self.DIALOG_WIDTH / 2, 100)
        self.army_title.move(0, 10)
        self.army_title.setAlignment(Qt.AlignCenter)

        self.soldier_image = QLabel(self)
        self.soldier_image.setPixmap(QPixmap(resources.img_army_picture))
        self.soldier_image.resize(self.DIALOG_WIDTH / 2, 170)
        self.soldier_image.move(0, 80)
        self.soldier_image.setAlignment(Qt.AlignCenter)

        self.name_input = StyledLineEdit(self)
        self.name_input.resize(180, 32)
        self.name_input.move(int(self.DIALOG_WIDTH / 2) + 10, 35)
        self.name_input.setPlaceholderText("성명")

        self.enter_day_input = StyledLineEdit(self)
        self.enter_day_input.resize(180, 32)
        self.enter_day_input.move(int(self.DIALOG_WIDTH / 2) + 10, 70)
        self.enter_day_input.setPlaceholderText("입영일(YYYY-MM-DD)")

        self.belonging_input = QComboBox(self)
        self.belonging_input.resize(180, 32)
        self.belonging_input.move(int(self.DIALOG_WIDTH / 2) + 10, 105)
        self.belonging_input.setStyleSheet('background-color: {}; Color: {}; '
                                           'border-radius: 2px; border: 1px solid {}; padding: 6px;'
                                           .format(resources.color_white,
                                                   resources.color_login_activity_text,
                                                   resources.color_text_field_border))
        self.belonging_input.setFont(QFont('a어린왕자M', 12))
        for belonging in self.belongings_map:
            self.belonging_input.addItem(belonging)

        self.birthday_input = StyledLineEdit(self)
        self.birthday_input.resize(180, 32)
        self.birthday_input.move(int(self.DIALOG_WIDTH / 2) + 10, 140)
        self.birthday_input.setPlaceholderText("생일(YYYY-MM-DD)")

        self.add_button = StyledButton(self)
        self.add_button.setText('Add')
        self.add_button.resize(180, 40)
        self.add_button.move(int(self.DIALOG_WIDTH / 2) + 10, 194)
        self.add_button.set_font_size(12)
        self.add_button.set_on_click(self.add_soldier)

        self.close_button = QLabel(self)
        self.close_button.setPixmap(QPixmap(resources.img_close))
        self.close_button.setScaledContents(True)
        self.close_button.resize(30, 30)
        self.close_button.move(370, 0)
        self.close_button.mouseReleaseEvent = lambda _: self.on_click_close()

    def on_click_close(self):
        self.on_closed()
        self.close()

    def add_soldier(self):
        name = self.name_input.text()
        enter_date = self.enter_day_input.text()
        belonging_code = self.belongings_map[self.belonging_input.currentText()]
        birth = self.birthday_input.text()

        date_format = re.compile('\d{4}-\d{2}-\d{2}')

        if name == '' or enter_date == '' or belonging_code == '' or birth == '' or \
                date_format.match(enter_date) is None or date_format.match(birth) is None:
            QMessageBox.warning(self, "ERROR", "훈련병 정보가 잘못되었습니다")
            return

        session = TheCampSessionManager().get_instance().get_session()
        main_client = MainClient(session)
        main_client.add_train_unit(name, birth, belonging_code, enter_date)
        main_client.join_cafe(name, birth.replace('-', ''), enter_date.replace('-', ''))

        self.on_closed()
        self.close()
