from enum import Enum


class TaskStatusEnum(Enum):
    Pending = 0
    Executed = 1
    Rejected = 2
    Deleted = 3
    Skipped = 4
