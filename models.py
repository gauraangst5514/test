from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    id: int
    title: str
    is_completed: bool
    priority: int  # 1 (high) to 5 (low)

class TaskDatabase:
    def __init__(self):
        self.tasks: List[Task] = []
        
    def add_task(self, task: Task):
        self.tasks.append(task)
        
    def get_all(self):
        return self.tasks
