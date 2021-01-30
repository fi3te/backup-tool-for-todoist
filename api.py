from typing import Tuple

import requests

import settings
from model import Data

SYNC_ENDPOINT = 'https://api.todoist.com/sync/v8/sync'


def _prepared_payload() -> dict:
    return {
        'token': settings.TOKEN,
        'sync_token': '*',
        'resource_types': '["projects", "items"]'
    }


def load() -> Tuple[Data, dict]:
    response = requests.post(SYNC_ENDPOINT, _prepared_payload())
    content = response.json()
    return Data(**content), content
