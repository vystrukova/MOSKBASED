import re
import requests
from bs4 import BeautifulSoup

from .api_client import ApiClient
from .info import Info


class SedApi(ApiClient):

    BASE_URL = Info.base_url
    MONT_URL = Info.mont_url
    AUTH_ADD = Info.auth_add
    GROUP_ID = Info.group_id
    USER_ID = Info.user_id
    PASSWORD = Info.password

    @classmethod
    def autorization_user(cls, params: dict = None):
        response = ApiClient.post_request(url=cls.BASE_URL + cls.AUTH_ADD, params=params)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        match = soup.find('a', href=re.compile(r'\?DNSID='))
        dnsid = match['href'].split('=')[1]
        return response, dnsid

    @classmethod
    def get_folder_list(cls, url: str, dnsid: str):
        query = """
            {
                folderList(parentId:null) {
                    list {
                        id
                        name
                        hasDocuments
                    }
                }
            }
        """
        headers = {
            'User-Agent': 'MONT / 4.9 Xiaomi Mi 9T, Android 11'
        }
        response = cls.post_request_mont(
            url=url,
            data={'DNSID': dnsid, 'q': query},
            headers=headers,
        )
        return response.json()
