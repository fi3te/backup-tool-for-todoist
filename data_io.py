import json
import os
from datetime import datetime
from typing import Optional

import constants
from model import Data


def _file_path(file_name: str): return f'{constants.BACKUP_FOLDER_PATH}/{file_name}'


def _file(file_name: str, mode: str): return open(_file_path(file_name), mode, encoding='utf-8')


def _create_backup_folder_if_necessary() -> None:
    if not os.path.isdir(constants.BACKUP_FOLDER_PATH):
        os.makedirs(constants.BACKUP_FOLDER_PATH)


def new_file_name_without_file_extension() -> str:
    return f'{datetime.now().strftime("%Y%m%d_%H%M")}'


def dump_json(file_name_without_file_extension: str, content: dict) -> None:
    _create_backup_folder_if_necessary()
    with _file(file_name_without_file_extension + '.json', 'w') as file:
        json.dump(content, file)


def dump_csv(file_name_without_file_extension: str, data: Data) -> None:
    _create_backup_folder_if_necessary()
    with _file(file_name_without_file_extension + '.csv', 'w') as file:
        separator = ';'

        header = separator.join([
            'Project',
            'Task',
            'Priority',
            'Date',
            'Date string',
            'Is recurring'
        ])
        file.write(f'{header}\n')

        for project in data.projects:
            items = [item for item in data.items if project.id == item.project_id]
            for item in items:
                values = [
                    project.name,
                    item.content,
                    str(item.priority),
                    item.due.date,
                    item.due.string,
                    str(item.due.is_recurring)
                ]
                line = separator.join(values)
                file.write(f'{line}\n')


def read_token(token_file_path: Optional[str], fallback: str) -> str:
    if token_file_path is None or not os.path.isfile(token_file_path):
        return fallback
    else:
        with open(token_file_path, 'r', encoding='utf-8') as file:
            return file.read()
