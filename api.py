from typing import Tuple, Optional

import requests

import constants
from model import Data


def _prepared_payload() -> dict:
    return {
        'sync_token': '*',
        'resource_types': '["projects", "items"]'
    }


def load() -> Tuple[Optional[Data], dict]:
    headers = {'Authorization': f'Bearer {constants.TOKEN}'}
    response = requests.post(constants.SYNC_ENDPOINT, _prepared_payload(), headers=headers)
    content = response.json()
    try:
        data = Data(**content)
        return data, content
    except AttributeError:
        return None, content
