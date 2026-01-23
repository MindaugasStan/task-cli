from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    def to_dict(self):
        task_dictionary = asdict(self)
        task_dictionary['created_at'] = self.created_at.isoformat()
        task_dictionary['updated_at'] = self.updated_at.isoformat()
        return task_dictionary