import json
import re
from datetime import datetime

from bs4 import BeautifulSoup
from client.thecamp_client import TheCampClient
from data.soldier import Soldier
from utils.utils import split_content_if_needed


class MainClient(TheCampClient):
    def __init__(self, session):
        super().__init__(session)

    # 우리 PK는 edu_seq인데.. 여긴 name.. 레거시..
    def send_letter(self, name, title, content):
        cafes = self.get_cafes()
        if name not in cafes:
            print(f'No Cafe with name: [{name}].')
            return False
        if cafes[name] is None:
            print(f'Cafe[{name}] is not open yet.')
            return False

        for splited_content in split_content_if_needed(content):
            self._send(cafes, name, title, splited_content)
        return True

    def _send(self, cafes, name, title, content):
        mgr_seq = self._get_mgr_seq(*cafes[name])
        endpoint = '/consolLetter/insertConsolLetterA.do'
        data = {
            'boardDiv': '',
            'tempSaveYn': 'N',
            'sympathyLetterEditorFileGroupSeq': '',
            'fileGroupMgrSeq': '',
            'fileMgrSeq': '',
            'sympathyLetterMgrSeq': '',
            'traineeMgrSeq': mgr_seq,
            'sympathyLetterSubject': title,
            'sympathyLetterContent': content,
        }

        result = self._post(endpoint, data)
        print(result)

    def get_cafes(self):
        endpoint = '/eduUnitCafe/viewEduUnitCafeMain.do'
        data = {}
        result = self._post(endpoint, data)
        soup = BeautifulSoup(result, 'html.parser')

        cafe_table = {}

        cafes = soup.select('.cafe-card-box')
        for cafe in cafes:
            name_div = cafe.select('.profile-wrap .id span')[0]
            name = name_div.text.split()[0]

            buttons = cafe.select('.btn-wrap')[0].find_all('a')

            for button in buttons:
                if button.text == '위문편지':
                    regex = re.compile('\'\d+\'')
                    codes = regex.findall(button['href'])

                    edu_seq, train_unit_code = map(lambda x: int(x[1:-1]), codes)
                    cafe_table[name] = (edu_seq, train_unit_code)
                    break
            else:
                cafe_table[name] = None
                continue

        return cafe_table

    def get_soldier_data(self):
        endpoint = '/eduUnitCafe/viewEduUnitCafeMain.do'
        data = {}
        result = self._post(endpoint, data)
        soup = BeautifulSoup(result, 'html.parser')

        solder_data = []

        cafes = soup.select('.cafe-card-box')
        for cafe in cafes:
            name_div = cafe.select('.profile-wrap .id span')[0]
            name = name_div.text.split()[0]

            days_info_div = cafe.select('.profile-wrap .cafe-sh-date span')
            entrance_day_div = days_info_div[0].select('em')[0]
            entrance_day = datetime.strptime(entrance_day_div.text.strip(), "%Y.%m.%d")

            if len(days_info_div) == 1:
                solder_data.append(Soldier(name, entrance_day, is_cafe_entranced=False))
                continue

            complete_day_div = days_info_div[1].select('em')[0]
            complete_day = datetime.strptime(complete_day_div.text.strip(), "%Y.%m.%d")

            edu_seq, train_unit_code = None, None
            buttons = cafe.select('.btn-wrap')[0].find_all('a')

            for button in buttons:
                if button.text == '위문편지':
                    regex = re.compile('\'\d+\'')
                    codes = regex.findall(button['href'])

                    edu_seq, train_unit_code = map(lambda x: x[1:-1], codes)
                    break

            solder_data.append(Soldier(name, entrance_day, complete_day, edu_seq, train_unit_code))
        return solder_data

    def _get_mgr_seq(self, edu_seq, train_unit_code):
        endpoint = '/consolLetter/viewConsolLetterMain.do'
        data = {
            'trainUnitEduSeq': edu_seq,
            'trainUnitCd': train_unit_code,
        }
        result = self._post(endpoint, data)
        soup = BeautifulSoup(result, 'html.parser')

        letter_box = soup.select('.letter-card-box')[0]
        regex = re.compile('\'\d+\'')
        codes = regex.findall(letter_box['href'])

        mgr_seq = map(lambda x: int(x[1:-1]), codes)
        return mgr_seq

    def get_group_code(self, group_name):
        group_code_table = {
            '육군': '0000010001',
            '해군': '0000010002',
            '공군': '0000010003',
            '해병대': '0000010004',
        }
        if group_name not in group_code_table:
            return ''
        return group_code_table[group_name]

    def get_train_unit_table(self, group_name):
        endpoint = '/join/selectTrainUnitListA.do'
        data = {
            'grpCd': self.get_group_code(group_name),
        }
        result = self._post(endpoint, data)
        result = json.loads(result, encoding='utf-8')

        unit_table = {}
        for unit in result['trainUnitList']:
            unit_table[unit['trainUnitNm']] = unit['trainUnitCd']
        return unit_table

    def get_relation_code(self, relation_name):
        relation_code_table = {
            '부모': '0000420001',
            '형제/자매': '0000420002',
            '배우자': '0000420003',
            '친척': '0000420004',
            '애인': '0000420005',
            '친구/지인': '0000420006',
            '팬': '0000420007',
        }
        if relation_name not in relation_code_table:
            return ''
        return relation_code_table[relation_name]

    def __get_iuid(self):
        endpoint = '/missSoldier/viewMissSoldierSearch.do'
        result = self._post(endpoint, {})
        soup = BeautifulSoup(result, 'html.parser')
        return soup.select('#mainForm input')[0].get('value')

    # birth/enter_date format: YYYY-MM-DD
    def add_train_unit(self, name, birth, belonging_code, enter_date):
        endpoint = '/missSoldier/insertDirectMissSoldierA.do'
        iuid = self.__get_iuid()
        data = {
            'iuid': iuid,
            'missSoldierClassCdNm': '예비군인/훈련병',
            'grpCdNm': '육군',
            'missSoldierClassCd': '0000490001',
            'grpCd': '0000010001',
            'name': name,
            'birth': birth,
            'trainUnitCd': belonging_code,
            'enterDate': enter_date,
            'missSoldierRelationshipCd': '0000420006',
            'countryCode': '39|+82',
        }
        self._post(endpoint, data)

    def __get_reg_order(self):
        endpoint = '/main/viewWebMain.do'
        result = self._post(endpoint, {})
        soup = BeautifulSoup(result, 'html.parser')
        return soup.select(".btn-main-center")[-1].select("a")[0].get('href').split('\'')[1]

    # birth/enter_date format: YYYYMMDD
    def join_cafe(self, name, birth, enter_date):
        endpoint = '/main/cafeCreateCheckA.do'
        reg_order = self.__get_reg_order()
        data = {
            'regOrder': reg_order,
            'name': name,
            'birth': birth,
            'enterDate': enter_date,
            'trainUnitCd': '20020191700',
            'trainUnitTypeCd': '0000140001',
            'grpCd': '0000010001',
            'traineeRelationshipCd': '0000420006',
        }
        result = self._post(endpoint, data)
        result = json.loads(result)
        return result
