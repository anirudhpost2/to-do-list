class Task:
    def __init__(self, title:str):
        self.title = title
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
        print(self)

    def __str__(self):
        status = "Completed" if self.completed else " "
        return f"[{status}] {self.title}"