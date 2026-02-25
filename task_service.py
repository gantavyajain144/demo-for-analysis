from models import Task
from utils import generate_id

class TaskService:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task_id = generate_id()
        task = Task(task_id, title)
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks