from datetime import date


class Soldier:
    name: str
    entrance_date: date
    complete_date: date
    edu_seq: str
    train_unit_code: str
    is_cafe_entranced: bool

    def __init__(self, name, entrance_date, complete_date=None, edu_seq=None, train_unit_code=None, is_cafe_entranced=True):
        self.name = name
        self.entrance_date = entrance_date
        self.complete_date = complete_date
        self.edu_seq = edu_seq
        self.train_unit_code = train_unit_code
        self.is_cafe_entranced = is_cafe_entranced
