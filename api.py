from typing import Tuple, Optional

import requests

import constants
from model import Data


def _prepared_payload() -> dict:
    return {
        'token': constants.TOKEN,
        'sync_token': '*',
        'resource_types': '["projects", "items"]'
    }


def load() -> Tuple[Optional[Data], dict]:
    response = requests.post(constants.SYNC_ENDPOINT, _prepared_payload())
    content = response.json()
    try:
        data = Data(**content)
        return data, content
    except AttributeError:
        return None, content
