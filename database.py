import sqlite3
from config import Config

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("tasks.db")

    def save_task(self, task):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (id, title, status) VALUES (?, ?, ?)",
            (task.id, task.title, task.status)
        )
        self.connection.commit()