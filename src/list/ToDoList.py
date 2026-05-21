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

    def display_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty!")
            return

        print("\n--- Current To-Do List ---")
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")
        print("--------------------------\n")