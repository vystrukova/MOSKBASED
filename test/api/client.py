import requests

import info


class ApiClientException(Exception):
    ...

class ApiClient:
    def __init__(self, base_url: str):
        #, login: str, password: str, organization: str
        self.base_url = base_url

        #self.organization = info.organization_api
        #self.login = info.login_api
        #self.password = info.password_api

        #self.session = requests.Session()

    def post_login(self):
        pass

    def get_token(self):
        headers = requests.get(url=self.base_url).headers
        pass


c = ApiClient(base_url='https://mosedo.mos.ru/auth.php?uri=%2F')
c.get_token()
pass