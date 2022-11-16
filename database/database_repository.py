from database.soldier_database_manager import SoldierLetterDatabaseManager


class DatabaseRepository:
    __instance = None
    __create_key = object()

    soldier_letter_database: SoldierLetterDatabaseManager

    def __init__(self, key=None):
        if key == self.__create_key:
            assert("Do not create DatabaseRepository instance directly. Use DatabaseRepository.get_instance() instead.")
        self.soldier_letter_database = SoldierLetterDatabaseManager.get_instance()

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = DatabaseRepository(cls.__create_key)
        return cls.__instance
