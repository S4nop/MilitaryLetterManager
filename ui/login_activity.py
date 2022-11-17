from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from helper.config_helper import ConfigHelper
from res import resources
from ui.main_activity import MainActivity
from ui.widgets.styled_button import StyledButton
from ui.widgets.styled_text_field import StyledLineEdit
from utils.utils import move_window_to_center
from client.login_client import LoginClient
from manager.thecamp_session_manager import TheCampSessionManager


class LoginActivity(QMainWindow):
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 380

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.show()
        self.__check_has_auto_login_info()

    def __init_ui(self):
        self.setWindowTitle('Login')
        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet('background-color: {};'.format(resources.color_gray_bg))
        move_window_to_center(self)

        self.title = QLabel("THE CAMP", self)
        self.title.setFont(QFont('a몬스터', 40))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.resize(self.WINDOW_WIDTH, 50)
        self.title.move(0, 50)
        self.title.setStyleSheet('Color: {}'.format(resources.color_primary))

        self.id_input = StyledLineEdit(self)
        self.id_input.resize(300, 44)
        self.id_input.move(50, 140)

        self.pw_input = StyledLineEdit(self)
        self.pw_input.setEchoMode(QLineEdit.Password)
        self.pw_input.resize(300, 44)
        self.pw_input.move(50, 190)

        self.login_button = StyledButton(self)
        self.login_button.set_text('Login')
        self.login_button.set_on_click(self.__login)
        self.login_button.resize(300, 44)
        self.login_button.move(50, 250)

        self.stay_login = QCheckBox("Stay Signed in", self)
        self.stay_login.move(50, 290)
        self.stay_login.setFont(QFont('Roboto', 10))
        self.stay_login.setStyleSheet('QCheckBox { background-color: rgba(0, 0, 0, 0); Color: #575757; } ')

        self.close_button = QLabel(self)
        self.close_button.setPixmap(QPixmap(resources.img_close))
        self.close_button.setScaledContents(True)
        self.close_button.resize(30, 30)
        self.close_button.move(360, 10)
        self.close_button.mouseReleaseEvent = self.close

    def __check_has_auto_login_info(self):
        is_auto_login, user_id, pw = ConfigHelper.get_auto_login_info()
        if is_auto_login:
            self.id_input.setText(user_id)
            self.pw_input.setText(pw)
            self.stay_login.setChecked(is_auto_login)
            self.__login()

    def __login(self):
        user_id = self.id_input.text()
        pw = self.pw_input.text()
        
        login_client = LoginClient()
        session = login_client.login(user_id, pw)
        if session is not None:
            if self.stay_login.isChecked():
                ConfigHelper.set_auto_login(user_id, pw)
            else:
                ConfigHelper.unset_auto_login()

            TheCampSessionManager().get_instance().set_session(session)
            main = MainActivity()
            main.show()
            self.close()
        else:
            QMessageBox.warning(self, "ERROR", "로그인 실패")

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key_Return:
            self.__login()
