import sqlite3


class SettingDatabaseManager:
    __instance = None
    __create_key = object()

    __db_path = "settings.db"

    def __init__(self, key=None):
        if key == self.__create_key:
            assert("Do not create SettingDatabaseManager instance directly. Use DatabaseRepository.solder_database instead.")
        self.connection = sqlite3.connect(self.__db_path)
        self.cursor = self.connection.cursor()

    @classmethod
    def get_instance(cls):
        if SettingDatabaseManager.__instance is None:
            SettingDatabaseManager.__instance = SettingDatabaseManager(cls.__create_key)
        return SettingDatabaseManager.__instance

    def __create_settings_database(self):
        pass
