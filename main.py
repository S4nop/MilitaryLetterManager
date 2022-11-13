import sys

from PyQt5.QtWidgets import QApplication

from helper.font_initalize_helper import FontInitializeHelper
from ui.login_activity import LoginActivity
from ui.main_activity import MainActivity
from ui.soldier_info_dialog import SoldierInfoDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    FontInitializeHelper.init_fonts()
    login_activity = LoginActivity()
    
    sys.exit(app.exec_())