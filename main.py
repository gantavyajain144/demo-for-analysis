from task_service import TaskService

def main():
    service = TaskService()
    service.add_task("Learn AI")
    service.add_task("Build Analyzer")

    tasks = service.get_all_tasks()
    for task in tasks:
        print(f"{task.id} - {task.title} - {task.status}")

if __name__ == "__main__":
    main()