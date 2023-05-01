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
