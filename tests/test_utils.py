import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Task
from utils import filter_active_high_priority_tasks, sort_tasks_by_priority

def test_filter_active_high_priority_tasks():
    tasks = [
        Task(1, "High priority active", False, 1),
        Task(2, "Low priority active", False, 5),
        Task(3, "High priority completed", True, 1),
        Task(4, "Low priority completed", True, 4),
        Task(5, "Medium-high priority active", False, 2)
    ]
    
    result = filter_active_high_priority_tasks(tasks)
    
    # Should only return tasks 1 and 5
    assert len(result) == 2, f"Expected 2 tasks, got {len(result)}"
    
    ids = [t.id for t in result]
    assert 1 in ids
    assert 5 in ids
    assert 2 not in ids
    assert 3 not in ids
    assert 4 not in ids
