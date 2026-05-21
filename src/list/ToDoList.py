from src.tasks.Task import Task
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task:Task):
        self.tasks.append(task)

    def remove_task(self, index:int):
       if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed task: '{removed.title}'")
       else:
            print("Invalid task index.")