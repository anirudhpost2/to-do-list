from datetime import datetime
from .Task import Task

class TimedTask(Task):
    def __init__(self, title:str, due_date:str):
        super().__init__(title)
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

    def mark_completed(self):
        super().mark_completed()

        today = datetime.today().date()
        if today <= self.due_date:
            print(f"Task completed on time! (Due: {self.due_date})")
        else:
            print(f"Task completed late! (Due: {self.due_date})")

    def __str__(self):
        status = "Completed" if self.completed else " "
        return f"[{status}] {self.title} (Due: {self.due_date})"