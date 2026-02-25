from models import Task
from utils import generate_id
import uuid
class TaskService:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task_id = str(uuid.uuid4())  # Or use a database sequence if available
        task = Task(task_id)
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks