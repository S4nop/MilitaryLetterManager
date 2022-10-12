import sqlite3

from data.soldier import Soldier


class SoldierDatabaseManager:
    __instance = None
    __create_key = object()

    __db_path = "soldier.db"

    def __init__(self, key=None):
        if key == self.__create_key:
            assert("Do not create SoldierDatabaseManager instance directly. Use DatabaseRepository.solder_database instead.")
        self.connection = sqlite3.connect(self.__db_path)
        self.cursor = self.connection.cursor()

    @classmethod
    def get_instance(cls):
        if SoldierDatabaseManager.__instance is None:
            SoldierDatabaseManager.__instance = SoldierDatabaseManager(cls.__create_key)
        return SoldierDatabaseManager.__instance

    def __create_soldier_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS soldiers
            (edu_seq TEXT PRIMARY KEY, name TEXT NOT NULL, news_choice_status INTEGER NOT NULL DEFAULT 0)''')
        self.connection.commit()

    def add_soldier(self, soldier: Soldier):
        self.cursor.execute('''INSERT INTO soldiers(edu_seq, name, news_choice_status)
            VALUES(?, ?, ?)''', (soldier.edu_seq, soldier.name, 0))
        self.connection.commit()

    def remove_soldier(self, soldier: Soldier):
        self.cursor.execute('''DELETE FROM soldiers WHERE edu_seq=?''', (soldier.edu_seq,))
        self.connection.commit()

    def update_message_choice(self, soldier: Soldier, news_choice_status: int):
        self.cursor.execute('''UPDATE soldiers SET news_choice_status=? WHERE edu_seq=?''',
                            (news_choice_status, soldier.edu_seq))
        self.connection.commit()

    def get_soldiers(self):
        self.cursor.execute('''SELECT * FROM soldiers''')
        return self.cursor.fetchall()

    def get_soldier(self, soldier: Soldier):
        self.cursor.execute('''SELECT * FROM soldiers WHERE edu_seq=?''', (soldier.edu_seq,))
        return self.cursor.fetchone()

    def __del__(self):
        self.connection.close()
