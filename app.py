from models import TaskDatabase, Task
from utils import filter_active_high_priority_tasks, sort_tasks_by_priority

def run_app():
    db = TaskDatabase()
    db.add_task(Task(1, "Fix database", False, 1))
    db.add_task(Task(2, "Update README", True, 4))
    db.add_task(Task(3, "Call client", False, 2))
    db.add_task(Task(4, "Buy milk", False, 5))
    
    print("All tasks:", db.get_all())
    
    critical_tasks = filter_active_high_priority_tasks(db.get_all())
    print("Critical active tasks:", critical_tasks)

if __name__ == "__main__":
    run_app()
