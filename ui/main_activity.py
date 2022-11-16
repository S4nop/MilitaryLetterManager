import time
from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QListWidget, QListView, QListWidgetItem, \
    QAbstractItemView

from client.main_client import MainClient
from data.news_choice import NewsChoice
from data.soldier import Soldier
from database.database_repository import DatabaseRepository
from helper.news_crawl_helper import NaverNewsType, get_naver_news_titles
from helper.tray_helper import TrayHelper
from manager.schedule_manager import ScheduleManager
from manager.thecamp_session_manager import TheCampSessionManager
from res import resources
from ui.add_soldier_dialog import AddSoldierDialog
from ui.soldier_info_dialog import SoldierInfoDialog
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
        self.__update_soldier_list()
        self.__draw_exit_button()
        self.__draw_tray_button()
        self.__start_letter_scheduler()
        self.__set_tray_icon()
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
        self.__update_list_items(soldier_list)

    def __update_soldier_list(self):
        self.solder_list_viewmodel.solder_list.value = self.main_client.get_soldier_data()

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

    def __draw_tray_button(self):
        self.tray_button = QLabel(self)
        self.tray_button.setPixmap(QPixmap(resources.img_to_tray))
        self.tray_button.move(960, 480)
        self.tray_button.resize(150, 150)
        self.tray_button.mousePressEvent = lambda _: self.__move_to_tray()

    def __update_list_items(self, soldier_data):
        self.__fetch_soldier_db(soldier_data)
        soldier_list = []
        for soldier in soldier_data:
            if not soldier.is_cafe_entranced:
                continue
            soldier_list.append(SoldierCard(self, soldier, self.on_click_soldier_card))
        soldier_list.append(AddActionCard(self, lambda: self.on_click_add_soldier_card()))

        self.list_widget.clear()
        for soldier_item in soldier_list:
            list_item = QListWidgetItem(self.list_widget)
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, soldier_item)
            list_item.setSizeHint(soldier_item.sizeHint())

    def __fetch_soldier_db(self, soldier_list):
        soldier_db = DatabaseRepository.get_instance().soldier_letter_database
        soldier_letter_info_list = soldier_db.get_all_infos()
        edu_seq_list_in_db = [soldier.edu_seq for soldier in soldier_letter_info_list]
        for soldier in soldier_list:
            if not soldier.is_cafe_entranced:
                continue
            if soldier.edu_seq not in edu_seq_list_in_db:
                soldier_db.add_soldier(soldier)

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

    def __update_soldier_news_choice(self, letter_info, news_choice):
        soldier_letter_db = DatabaseRepository.get_instance().soldier_letter_database
        letter_info.letter_news_category = news_choice
        soldier_letter_db.update_soldier_letter_info(letter_info)

    def __on_done_adding_soldier(self):
        # 프로그램이 아예 멈추지 않게 하기 위해 쓰레드로 넘겨야 함
        # 시간상의 문제로 일단 이렇게 처리
        time.sleep(1)
        self.__update_soldier_list()

    def __start_letter_scheduler(self):
        scheduler = ScheduleManager.get_instance()
        scheduler.set_schedule("13:00")
        scheduler.add_job(self.__send_letter)
        scheduler.run()

    def __create_letter_content(self, news_choice: NewsChoice):
        content = ''
        if news_choice.get_politic_flag():
            content += '\n\n' + get_naver_news_titles(NaverNewsType.POLITIC)
        if news_choice.get_economy_flag():
            content += '\n\n' + get_naver_news_titles(NaverNewsType.ECONOMY)
        if news_choice.get_society_flag():
            content += '\n\n' + get_naver_news_titles(NaverNewsType.SOCIETY)
        if news_choice.get_world_flag():
            content += '\n\n' + get_naver_news_titles(NaverNewsType.WORLD)
        if news_choice.get_itscience_flag():
            content += '\n\n' + get_naver_news_titles(NaverNewsType.ITSCIENCE)
        if news_choice.get_lifeculture_flag():
            content += '\n\n' + get_naver_news_titles(NaverNewsType.LIFECULTURE)
        return content

    def __send_letter(self):
        soldier_letter_db = DatabaseRepository.get_instance().soldier_letter_database
        soldier_list = self.solder_list_viewmodel.solder_list.value
        for soldier in soldier_list:
            letter_info = soldier_letter_db.get_soldier_letter_info(soldier)
            if letter_info.letter_news_category.to_int_value() == 0:
                return
            content = self.__create_letter_content(letter_info.letter_news_category)
            self.main_client.send_letter(soldier.name, "오늘의 뉴스", content)
        self.tray_icon.notification('편지 전송 완료')

    def __set_tray_icon(self):
        self.tray_icon = TrayHelper('MilitaryLetter', 'TheCamp Letter Helper')\
            .set_icon(resources.logo)\
            .add_menu('열기', self.__restore_from_tray, is_onclick=True)\
            .add_menu('종료', lambda: self.__fade_out_exit())
        self.tray_icon.run()

    def __restore_from_tray(self):
        self.show()

    def __move_to_tray(self):
        self.hide()

    def __fade_out_exit(self):
        self.tray_icon.stop()
        ScheduleManager.get_instance().kill()
        for i in range(50):
            i = i / 50
            self.setWindowOpacity(1 - i)
            time.sleep(0.005)
        exit(0)

    def on_click_soldier_card(self, soldier: Soldier):
        date_diff = soldier.complete_date - datetime.today()
        letter_info = DatabaseRepository.get_instance().soldier_letter_database.get_soldier_letter_info(soldier)
        dialog = SoldierInfoDialog(self, soldier.name, date_diff.days, letter_info,
                                   lambda letter_choice: self.__update_soldier_news_choice(letter_info, letter_choice))
        dialog.setModal(True)
        dialog.exec()

    def on_click_add_soldier_card(self):
        dialog = AddSoldierDialog(self, lambda: self.__on_done_adding_soldier())
        dialog.setModal(True)
        dialog.exec()
