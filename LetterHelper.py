import sys

from PyQt5.QtWidgets import QApplication

from helper.config_helper import ConfigHelper
from helper.font_initalize_helper import FontInitializeHelper
from ui.login_activity import LoginActivity

if __name__ == '__main__':
    app = QApplication(sys.argv)
    FontInitializeHelper.init_fonts()
    ConfigHelper.create_config_file()
    login_activity = LoginActivity()
    
    sys.exit(app.exec_())
