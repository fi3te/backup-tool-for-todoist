import json
import os
from datetime import datetime

from model import Data

BACKUP_FOLDER_PATH = './backup'


def _file_path(file_name: str): return f'{BACKUP_FOLDER_PATH}/{file_name}'


def _file(file_name: str, mode: str): return open(_file_path(file_name), mode, encoding='utf-8')


def _create_backup_folder_if_necessary() -> None:
    if not os.path.isdir(BACKUP_FOLDER_PATH):
        os.makedirs(BACKUP_FOLDER_PATH)


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
