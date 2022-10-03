import time
import schedule


class ScheduleManager:
    __instance = None
    __create_key = object()

    __job_queue = []
    __scheduler: schedule

    def __init__(self, key=None):
        if key == self.__create_key:
            assert("ScheduleManager is singleton class. Use ScheduleManager.get_instance() instead of ScheduleManager()")
        self.__scheduler = schedule

    @classmethod
    def get_instance(cls):
        if ScheduleManager.__instance is None:
            ScheduleManager.__instance = ScheduleManager(cls.__create_key)
        return ScheduleManager.__instance

    def add_job(self, job):
        self.__job_queue.append(job)

    def clear_job(self):
        self.__job_queue.clear()

    def set_schedule(self, time_):
        self.__scheduler.every().monday.at(time_).do(self.__run_job)
        self.__scheduler.every().tuesday.at(time_).do(self.__run_job)
        self.__scheduler.every().wednesday.at(time_).do(self.__run_job)
        self.__scheduler.every().thursday.at(time_).do(self.__run_job)
        self.__scheduler.every().friday.at(time_).do(self.__run_job)

    def run(self):
        self.__scheduler.run_pending()
        time.sleep(60)

    def __run_job(self):
        for job in self.__job_queue:
            job()

