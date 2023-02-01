import requests

import info


class ApiClientException(Exception):
    ...

class ApiClient:
    def __init__(self, base_url: str, login: str, password: str, organization: str):
        #, login: str, password: str, organization: str
        self.base_url = base_url

        self.organization = organization
        self.login = login
        self.password = password

        #self.session = requests.Session()

    def post_login(self):

        headers = {
            #'set-cookie' : 'auth_token=2823c0a8482d06a048b5f1cdf415291820b13be6'
        }

        data = {
            'group_id' : self.organization,
            'user_id' : self.login,
            'password' : self.password
        }

        login_request = requests.post(url='https://mosedo.mos.ru/auth.php?group_id=2', headers=headers, data=data)
        return login_request

    def get_dnsid(self):
        headers = requests.get(url=self.base_url).headers
        pass


c = ApiClient(base_url='https://mosedo.mos.ru/auth.php?group_id=2', organization=info.organization_api, login=info.login_api, password=info.password_api)
res = c.post_login()

