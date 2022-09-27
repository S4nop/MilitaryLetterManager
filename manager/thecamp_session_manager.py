import requests


class TheCampSessionManager:
    __instance = None
    __create_key = object()

    __session: requests.Session

    def __init__(self, key=None):
        if key == self.__create_key:
            assert("SessionManager is singleton class. Use SessionManager.get_instance() instead of SessionManager()")
        self.__session = requests.Session()

    @classmethod
    def get_instance(cls):
        if TheCampSessionManager.__instance is None:
            TheCampSessionManager.__instance = TheCampSessionManager(cls.__create_key)
        return TheCampSessionManager.__instance

    def set_session(self, session):
        self.__session = session

    def get_session(self):
        return self.__session