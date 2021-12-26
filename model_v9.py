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
    added_at: Optional[str]
    added_by_uid: any
    assigned_by_uid: any
    checked: Optional[bool]
    child_order: Optional[int]
    collapsed: Optional[bool]
    completed_at: Optional[str]
    content: Optional[str]
    day_order: Optional[int]
    description: Optional[str]
    due: Due
    id: Optional[int]
    in_history: Optional[bool]
    is_deleted: Optional[bool]
    labels: any
    parent_id: Optional[int]
    priority: Optional[int]
    project_id: Optional[int]
    responsible_uid: any
    section_id: Optional[int]
    sync_id: Optional[int]
    user_id: Optional[int]

    def __init__(self, **kwargs):
        _set_attributes(self, **kwargs)
        if isinstance(self.due, dict):
            self.due = Due(**self.due)


class Project:
    child_order: Optional[int]
    collapsed: Optional[bool]
    color: Optional[str]
    id: Optional[int]
    inbox_project: Optional[bool]
    is_archived: Optional[bool]
    is_deleted: Optional[bool]
    is_favorite: Optional[bool]
    name: Optional[str]
    parent_id: Optional[int]
    shared: Optional[bool]
    sync_id: Optional[int]
    team_inbox: Optional[bool]
    view_style: Optional[str]

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
