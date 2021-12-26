from typing import Optional

from argh import arg

import data_io

SYNC_ENDPOINT = 'https://api.todoist.com/sync/v9/sync'
TOKEN = 'no_token'
BACKUP_FOLDER_PATH = './backup'


def add_parameter(func):
    global TOKEN, BACKUP_FOLDER_PATH

    @arg('-t', '--token')
    @arg('-tp', '--token_file_path')
    def wrapper(token: str = TOKEN,
                token_file_path: str = None,
                backup_folder_path: str = BACKUP_FOLDER_PATH) -> Optional:
        global TOKEN, BACKUP_FOLDER_PATH
        if token is not None:
            TOKEN = token
        if token_file_path is not None:
            TOKEN = data_io.read_token(token_file_path, TOKEN)
        if backup_folder_path is not None:
            BACKUP_FOLDER_PATH = backup_folder_path

        print('Used parameters:')
        print(f'TOKEN: ...{TOKEN[-3:]}')
        print(f'BACKUP_FOLDER_PATH: {BACKUP_FOLDER_PATH}')
        print()
        return func()

    return wrapper
