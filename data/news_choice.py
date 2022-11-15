class NewsChoice:
    __choice_status: int

    @property
    def choice_status(self):
        return self.__choice_status

    def __init__(self):
        self.__choice_status = 0

    def set_politic_flag(self):
        self.__choice_status |= 1

    def get_politic_flag(self):
        return self.__choice_status & 1

    def set_economy_flag(self):
        self.__choice_status |= (1 << 1)

    def get_economy_flag(self):
        return self.__choice_status & (1 << 1)

    def set_society_flag(self):
        self.__choice_status |= (1 << 2)

    def get_society_flag(self):
        return self.__choice_status & (1 << 2)

    def set_lifeculture_flag(self):
        self.__choice_status |= (1 << 3)

    def get_lifeculture_flag(self):
        return self.__choice_status & (1 << 3)

    def set_world_flag(self):
        self.__choice_status |= (1 << 4)

    def get_world_flag(self):
        return self.__choice_status & (1 << 4)

    def set_itscience_flag(self):
        self.__choice_status |= (1 << 5)

    def get_itscience_flag(self):
        return self.__choice_status & (1 << 5)

    @staticmethod
    def from_int_value(choice_status: int):
        news_choice = NewsChoice()
        news_choice.__choice_status = choice_status
        return news_choice
