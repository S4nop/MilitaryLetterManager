from PyQt5.QtGui import QFontDatabase


class FontInitializeHelper:
    @staticmethod
    def init_fonts():
        font_db = QFontDatabase()
        font_db.addApplicationFont("./res/fonts/a꾸러기.ttf")
        font_db.addApplicationFont("./res/fonts/a몬스터.ttf")
        font_db.addApplicationFont("./res/fonts/a어린왕자M.ttf")
        font_db.addApplicationFont("./res/fonts/Roboto.ttf")
