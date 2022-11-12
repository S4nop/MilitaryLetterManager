import json

import requests

from client.thecamp_client import TheCampClient


class LoginClient(TheCampClient):
    def __init__(self, session=None):
        super().__init__(session)

    def login(self, userid, passwd):
        endpoint = '/login/loginA.do'
        data = {
            'state': 'email-login',
            'autoLoginYn': 'N',
            'userId': userid,
            'userPwd': passwd,
        }

        if self.session is None:
            self.session = requests.Session()

        result = self._post(endpoint, data)
        result = json.loads(result)

        if 'resultCd' in result and result['resultCd'] == '0000':
            print(f'Successfully Login! [{userid}]')
            return self.session
        print(f'Login failed. [{result["resultMsg"] if "resultMsg" in result else "Unknown Error"}]')
        return None
