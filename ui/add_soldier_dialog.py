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

    def __init__(self, parent):
        super().__init__(parent, Qt.WindowFlags(Qt.FramelessWindowHint))
        self.__init_ui()
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
        self.name_input.move(int(self.DIALOG_WIDTH / 2) + 10, 34)
        self.name_input.setPlaceholderText("성명")

        self.enter_day_input = StyledLineEdit(self)
        self.enter_day_input.resize(180, 32)
        self.enter_day_input.move(int(self.DIALOG_WIDTH / 2) + 10, 84)
        self.enter_day_input.setPlaceholderText("입영일(YYYY-MM-DD)")

        self.birthday_input = StyledLineEdit(self)
        self.birthday_input.resize(180, 32)
        self.birthday_input.move(int(self.DIALOG_WIDTH / 2) + 10, 134)
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
        self.close()

    def add_soldier(self):
        name = self.name_input.text()
        enter_date = self.enter_day_input.text()
        birth = self.birthday_input.text()

        session = TheCampSessionManager().get_instance().get_session()
        main_client = MainClient(session)
        main_client.add_train_unit(name, birth, enter_date)
        main_client.join_cafe(name, birth.replace('-', ''), enter_date.replace('-', ''))
        
        self.close()
