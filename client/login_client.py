import json

from client.thecamp_client import TheCampClient


class LoginClient(TheCampClient):
    def __init__(self, session):
        super().__init__(session)

    def login(self, userid, passwd):
        endpoint = '/login/loginA.do'
        data = {
            'state': 'email-login',
            'autoLoginYn': 'N',
            'userId': userid,
            'userPwd': passwd,
        }

        result = self._post(endpoint, data)
        result = json.loads(result)

        if 'resultCd' in result and result['resultCd'] == '0000':
            print(f'Successfully Login! [{userid}]')
            return True
        print(f'Login failed. [{result["resultMsg"] if "resultMsg" in result else "Unknown Error"}]')
        return False
