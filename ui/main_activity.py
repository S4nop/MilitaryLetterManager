import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QListWidget, QListView, QListWidgetItem, \
    QAbstractItemView

from client.main_client import MainClient
from manager.thecamp_session_manager import TheCampSessionManager
from res import resources
from ui.widgets.card.add_action_card import AddActionCard
from ui.widgets.card.soldier_card import SoldierCard
from utils.utils import move_window_to_center
from viewmodel.soldier_list_viewmodel import SoldierListViewModel


class MainActivity(QMainWindow):
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 700

    main_client: MainClient = None
    solder_list_viewmodel: SoldierListViewModel = None

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__init_client()
        self.__init_viewmodel()
        self.__update_list_items(None)
        self.__draw_exit_button()
        self.show()

    def __init_ui(self):
        self.setGeometry(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.__init_background()
        self.__init_list_view()
        move_window_to_center(self)

    def __init_client(self):
        session = TheCampSessionManager.get_instance().get_session()
        self.main_client = MainClient(session)

    def __init_viewmodel(self):
        self.solder_list_viewmodel = SoldierListViewModel()
        self.solder_list_viewmodel.solder_list.observe(self.__on_soldier_list_changed)

    def __on_soldier_list_changed(self, soldier_list):
        print(soldier_list)

    def __update_soldier_list(self):
        self.solder_list_viewmodel.solder_list = self.main_client.get_soldier_data()

    def __init_list_view(self):
        self.list_widget = QListWidget(self)
        self.list_widget.resize(1100, 340)
        self.list_widget.move(40, 40)
        self.list_widget.setFlow(QListView.LeftToRight)
        self.list_widget.setStyleSheet('background-color: {}; border: 0px'.format(resources.color_main_bg))
        self.list_widget.horizontalScrollBar().setStyleSheet('height: 0px')
        self.list_widget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list_widget.setSpacing(20)

        self.__draw_vanishing_line_end_of_list()

    def __draw_vanishing_line_end_of_list(self):
        self.listview_shadow = QLabel(self)
        self.listview_shadow.setPixmap(QPixmap(resources.img_listview_shadow))
        self.listview_shadow.move(1110, 60)
        self.listview_shadow.resize(70, 300)

    def __draw_exit_button(self):
        self.exit_button = QLabel(self)
        self.exit_button.setPixmap(QPixmap(resources.img_exit))
        self.exit_button.move(1080, 480)
        self.exit_button.resize(150, 150)
        self.exit_button.mousePressEvent = lambda _: self.__fade_out_exit()

    def __update_list_items(self, soldier_list):
        if soldier_list is None:
            soldier_list = [
                SoldierCard(self, '3', '우지은'),
                SoldierCard(self, '13', '류성희'),
                SoldierCard(self, '23', '신용준'),
                SoldierCard(self, '33', '윤상원'),
                SoldierCard(self, '43', '김민수'),
            ]
        soldier_list.append(AddActionCard(self))

        self.list_widget.clear()
        for soldier_item in soldier_list:
            list_item = QListWidgetItem(self.list_widget)
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, soldier_item)
            list_item.setSizeHint(soldier_item.sizeHint())

    def __init_background(self):
        self.bg_top = QLabel(self)
        self.bg_top.setAlignment(Qt.AlignHCenter)
        self.bg_top.resize(self.WINDOW_WIDTH, 420)
        self.bg_top.move(0, 0)
        self.bg_top.setStyleSheet('background-color: {}'.format(resources.color_main_bg))

        self.bg_bottom = QLabel(self)
        self.bg_bottom.setAlignment(Qt.AlignHCenter)
        self.bg_bottom.resize(self.WINDOW_WIDTH, 280)
        self.bg_bottom.move(0, 420)
        self.bg_bottom.setStyleSheet('background-color: {}'.format(resources.color_white))

        self.title = QLabel('THE CAMP', self)
        self.title.setFont(QFont('a몬스터', 56))
        self.title.move(60, 510)
        self.title.resize(self.WINDOW_WIDTH, 100)
        self.title.setStyleSheet('Color: {}'.format(resources.color_primary))

    def __fade_out_exit(self):
        for i in range(50):
            i = i / 50
            self.setWindowOpacity(1 - i)
            time.sleep(0.005)
        exit()