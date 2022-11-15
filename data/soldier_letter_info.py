from data.news_choice import NewsChoice


class SoldierLetterInfo:
    def __init__(self, edu_seq, last_sent_date, letter_count, letter_news_category):
        self.edu_seq = edu_seq
        self.last_sent_date = last_sent_date
        self.letter_count = letter_count
        self.letter_news_category = NewsChoice.from_int_value(letter_news_category)

    edu_seq: str
    last_sent_date: str
    letter_count: int
    letter_news_category: NewsChoice
