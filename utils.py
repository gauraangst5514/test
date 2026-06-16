from typing import List
from models import Task

def filter_active_high_priority_tasks(tasks: List[Task]) -> List[Task]:
    """
    Should return a list of active (not completed) tasks that have high priority (priority 1 or 2).
    """
    filtered = []
    for t in tasks:
        if not t.is_completed and t.priority <= 2:
            filtered.append(t)
    return filtered

def sort_tasks_by_priority(tasks: List[Task]) -> List[Task]:
    """Sort tasks by priority, highest (1) first."""
    return sorted(tasks, key=lambda x: x.priority)