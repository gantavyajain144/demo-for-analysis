from database import Database
from task_service import TaskService

class ReportService:

    def __init__(self):
        self.db = Database()
        self.task_service = TaskService()

    def generate_report(self):
        tasks = self.task_service.get_all_tasks()

        for task in tasks:
            print(f"{task.id} - {task.title} - {task.status}")