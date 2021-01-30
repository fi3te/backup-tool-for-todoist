from typing import List, Optional


def _set_attributes(obj, **kwargs):
    for key, value in kwargs.items():
        setattr(obj, key, value)


class Due:
    date: Optional[str]
    is_recurring: Optional[bool]
    lang: Optional[str]
    string: Optional[str]
    timezone: any

    def __init__(self, **kwargs):
        _set_attributes(self, **kwargs)


class Item:
    added_by_uid: any
    assigned_by_uid: any
    checked: Optional[int]
    child_order: Optional[int]
    collapsed: Optional[int]
    content: Optional[str]
    date_added: Optional[str]
    date_completed: any
    day_order: Optional[int]
    due: Due
    has_more_notes: Optional[bool]
    id: Optional[int]
    in_history: Optional[int]
    is_deleted: Optional[int]
    labels: any
    parent_id: any
    priority: Optional[int]
    project_id: Optional[int]
    responsible_uid: any
    section_id: any
    sync_id: any
    user_id: any

    def __init__(self, **kwargs):
        _set_attributes(self, **kwargs)
        if isinstance(self.due, dict):
            self.due = Due(**self.due)


class Project:
    child_order: Optional[int]
    collapsed: Optional[int]
    color: Optional[int]
    has_more_notes: Optional[bool]
    id: Optional[int]
    inbox_project: Optional[bool]
    is_archived: Optional[int]
    is_deleted: Optional[int]
    is_favorite: Optional[int]
    name: Optional[str]
    parent_id: Optional[int]
    shared: Optional[bool]
    sync_id: any

    def __init__(self, **kwargs):
        _set_attributes(self, **kwargs)


class Data:
    full_sync: Optional[bool]
    items: List[Item]
    projects: List[Project]
    sync_token: Optional[str]
    temp_id_mapping: Optional[dict]

    def __init__(self, **kwargs):
        _set_attributes(self, **kwargs)
        if isinstance(self.items, List) and len(self.items) > 0:
            self.items = list(map(lambda d: Item(**d), self.items))
        if isinstance(self.projects, List) and len(self.projects) > 0:
            self.projects = list(map(lambda d: Project(**d), self.projects))
