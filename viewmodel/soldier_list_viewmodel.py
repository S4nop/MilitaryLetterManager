from typing import List

from data.livedata import LiveData
from data.soldier import Soldier


class SoldierListViewModel:
    solder_list: LiveData[List[Soldier]] = None

    def __init__(self):
        self.solder_list = LiveData([])
