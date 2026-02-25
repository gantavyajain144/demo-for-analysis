import json
from report_service import ReportService
from database import Database
from models import Task

class AnalyticsService:

    def __init__(self):
        self.report_service = ReportService()
        self.database = Database()

    def export_tasks_to_json(self):
        tasks = self.report_service.task_service.get_all_tasks()

        task_data = []
        for task in tasks:
            task_data.append({
                "id": task.id,
                "title": task.title,
                "status": task.status
            })

        return json.dumps(task_data, indent=4)

    def count_completed_tasks(self):
        tasks = self.report_service.task_service.get_all_tasks()
        return len([t for t in tasks if t.status == "COMPLETED"])