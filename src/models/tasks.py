from enum import Enum


class TaskStatus(Enum):
    ACTIVE = 0
    COMPLETE = 1
    ARCHIVED = 2


class Task:
    def __init__(self, name, description, priority, status_id=0, category_id=0, ID=-1):
        self.ID = ID
        self.name = name
        self.description = description
        self.priority = priority
        self.status = TaskStatus(status_id)
        self.category_id = category_id

    def __repr__(self):
        return f'<Todo {self.name}>'

    def __str__(self):
        return f'{self.name} - {self.priority}'
