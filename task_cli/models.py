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
        task_dictionary["created_at"] = self.created_at.isoformat()
        task_dictionary["updated_at"] = self.updated_at.isoformat()
        return task_dictionary

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=data["id"],
            description=data["description"],
            status=TaskStatus(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )

    def update(
        self, description: str | None = None, status: TaskStatus | None = None
    ) -> None:
        """Update the task in memory"""
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return f"[{self.id}] {self.description} ({self.status.value})"
