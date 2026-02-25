from task_service import TaskService, Task

def main():
    service = TaskService()
try:
    service.add_task("Learn AI")
    service.add_task("Build Analyzer")

    tasks = service.get_all_tasks()
    for task in tasks:
        print(f"{task['id']} - {task['title']} - {task['status']}")
except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    main()