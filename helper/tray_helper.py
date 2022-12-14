import threading
import time
import pystray
from pystray import MenuItem as Item, Menu
from PIL import Image


class TrayHelper:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.icon = None
        self.menu_items = []
        self.it = None

    def run(self):
        threading.Thread(target=self.__create).start()
        self.notification('TheCamp Letter Helper Running')

    def stop(self):
        self.it.stop()

    def set_icon(self, ico_path):
        self.icon = Image.open(ico_path)
        return self

    def add_menu(self, name: str, action, is_onclick=False):
        self.menu_items.append(Item(name, action, default=is_onclick))
        return self

    def notification(self, msg):
        time.sleep(1)
        if self.it.HAS_NOTIFICATION:
            self.it.notify(self.title, msg)
        else:
            print('NO NOTI')

    def __create(self):
        self.it = pystray.Icon(self.name, self.icon, self.title,
                               menu=Menu(lambda: (item_ for item_ in self.menu_items)))
        self.it.run()
