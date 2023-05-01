import allure
import pytest
from api.utils import SedApi
from api.utils.user_fixture import generate_user


class TestMosedoApi(SedApi):

    @pytest.mark.API
    def test_autorization_api(self):
        user_info = generate_user()
        response, dnsid = self.autorization_user(params=user_info)
        assert response.status_code == 200
        assert dnsid is not None
        allure.attach(str(response.status_code), "status_code", allure.attachment_type.TEXT)
        allure.attach(dnsid, "DNSID", allure.attachment_type.TEXT)
