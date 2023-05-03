import pytest
import string
import random
import re

from .info import *
from .sed_api import SedApi


def generate_user() -> dict:
    user_info = {
        "group_id": Info.group_id,
        "user_id": Info.user_id,
        "password": Info.password
    }
    return user_info


@pytest.fixture(scope="function")
def autorized_client():
    # авторизуемся
    user_info = generate_user()
    response, dnsid = SedApi.autorization_user(user_info)
    assert response.status_code == 200, f"Не удалось авторизоваться. Response status code: {response.status_code}"
    assert dnsid is not None, "DNSID не получен после авторизации"

    yield response, dnsid
