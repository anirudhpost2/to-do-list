from src.tasks.* import Task, TimedTask
from .list.ToDoList import ToDoList
from datetime import datetime

def main():
    my_list = ToDoList()
    my_list.add_task(Task("Study for Data Structures"))
    my_list.add_task(TimedTask("Upload singing content", "2026-05-22"))
    my_list.add_task(TimedTask("Figure out what to do with my life", "2026-05-20"))

    my_list.display_tasks()

    my_list.tasks[0].mark_completed()
    my_list.tasks[1].mark_completed()
    my_list.tasks[2].mark_completed()

    my_list.display_tasks()

if __name__ == "__main__":
    main()