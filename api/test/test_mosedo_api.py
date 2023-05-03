import allure
import pytest
from api.utils import SedApi
import json
from  api.utils.info import *
from api.utils.user_fixture import autorized_client


class TestMosedoApi(SedApi):

    @pytest.mark.API()
    # используем фикстуру autorized_client
    def test_autorization_api(self, autorized_client):
        response, dnsid = autorized_client
        assert response.status_code == 200
        assert dnsid is not None
        allure.attach(str(response.status_code), "status_code", allure.attachment_type.TEXT)
        allure.attach(dnsid, "DNSID", allure.attachment_type.TEXT)

    @pytest.mark.skip
    @pytest.mark.API()
    def test_get_folder_list(self, autorized_client):
        # Получение ответа от сервера и dnsid из фикстуры autorized_client
        response, dnsid = autorized_client

        # Получение списка папок, используя переданный URL
        folder_list = self.get_folder_list(url=Info.mont_url, dnsid=dnsid)

        # Проверка статуса ответа
        assert response.status_code == 200
        allure.attach(str(response.status_code), "status_code", allure.attachment_type.TEXT)

        # Добавление отчетности о DNSID
        allure.attach(dnsid, "dnsid", allure.attachment_type.TEXT)
        allure.attach(response.request.url, "request_url", allure.attachment_type.TEXT)
        allure.attach(json.dumps(folder_list), "folder_list", allure.attachment_type.JSON)