import requests


class TheCampClient:
    host = 'https://www.thecamp.or.kr'
    session: requests.Session

    def __init__(self, session):
        self.session = session

    def _post(self, endpoint, data):
        response = self.session.post(self.host + endpoint, data=data)
        if response.status_code != 200:
            raise ConnectionError(f'Connection failed: [{response.status_code}] - {response.text}')
        return response.text
