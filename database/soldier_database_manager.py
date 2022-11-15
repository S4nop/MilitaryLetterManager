import sqlite3

from data.soldier import Soldier
from data.soldier_letter_info import SoldierLetterInfo


class SoldierLetterDatabaseManager:
    __instance = None
    __create_key = object()

    __db_path = "soldier_letter.db"

    def __init__(self, key=None):
        if key == self.__create_key:
            assert("Do not create SoldierLetterDatabaseManager instance directly. Use DatabaseRepository.solder_database instead.")
        self.connection = sqlite3.connect(self.__db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.__create_soldier_letter_database()

    @classmethod
    def get_instance(cls):
        if SoldierLetterDatabaseManager.__instance is None:
            SoldierLetterDatabaseManager.__instance = SoldierLetterDatabaseManager(cls.__create_key)
        return SoldierLetterDatabaseManager.__instance

    def __create_soldier_letter_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS soldier_letter
            (edu_seq TEXT PRIMARY KEY, last_sent_date TEXT NOT NULL, 
            letter_count INTEGER NOT NULL DEFAULT 0, news_choice_status INTEGER NOT NULL DEFAULT 0)''')
        self.connection.commit()

    def add_soldier(self, soldier: Soldier):
        self.cursor.execute('''INSERT INTO soldier_letter(edu_seq, last_sent_date, letter_count, news_choice_status)
            VALUES(?, ?, ?, ?)''', (soldier.edu_seq, "-", 0, 0))
        self.connection.commit()

    def remove_soldier(self, soldier: Soldier):
        self.cursor.execute('''DELETE FROM soldier_letter WHERE edu_seq=?''', (soldier.edu_seq,))
        self.connection.commit()

    def update_soldier_letter_info(self, soldier_letter_info: SoldierLetterInfo):
        self.cursor.execute('''UPDATE soldier_letter SET last_sent_date=?, letter_count=?, news_choice_status=?
            WHERE edu_seq=?''', (soldier_letter_info.last_sent_date, soldier_letter_info.letter_count,
                                 soldier_letter_info.letter_news_category.to_int_value(), soldier_letter_info.edu_seq))
        self.connection.commit()

    def update_message_choice(self, soldier: Soldier, news_choice_status: int):
        self.cursor.execute('''UPDATE soldier_letter SET news_choice_status=? WHERE edu_seq=?''',
                            (news_choice_status, soldier.edu_seq))
        self.connection.commit()

    def update_sent_letter_info(self, soldier: Soldier, last_sent_date: str, letter_count: int):
        self.cursor.execute('''UPDATE soldier_letter SET last_sent_date=?, letter_count=? WHERE edu_seq=?''',
                            (last_sent_date, letter_count, soldier.edu_seq))
        self.connection.commit()

    def get_all_infos(self):
        self.cursor.execute('''SELECT * FROM soldier_letter''')
        tuple_datas = self.cursor.fetchall()
        return [SoldierLetterInfo(*tuple_data) for tuple_data in tuple_datas]

    def get_soldier_letter_info(self, soldier: Soldier):
        self.cursor.execute('''SELECT * FROM soldier_letter WHERE edu_seq=?''', (soldier.edu_seq,))
        tuple_data = self.cursor.fetchone()
        return SoldierLetterInfo(*tuple_data)

    def __del__(self):
        self.connection.close()
