from PyQt5.QtWidgets import QMainWindow

from client.main_client import MainClient
from manager.thecamp_session_manager import TheCampSessionManager
from viewmodel.soldier_list_viewmodel import SoldierListViewModel


class MainActivity(QMainWindow):
    main_client: MainClient = None
    solder_list_viewmodel: SoldierListViewModel = None

    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__init_client()
        self.__init_viewmodel()
        self.show()

    def __init_ui(self):
        self.setWindowTitle('Main')
        self.setGeometry(300, 300, 300, 200)

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
