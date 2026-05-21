import src.tasks.Task as task_module
import src.tasks.TimedTask as timed_task_module
import src.list.ToDoList as list_module
from datetime import datetime

Task = task_module.Task
TimedTask = timed_task_module.TimedTask
ToDoList = list_module.ToDoList

def main():
    my_list = ToDoList()
    
    print("========================================")
    print("   Welcome to your Polymorphic To-Do!   ")
    print("========================================")

    while True:
        print("\n--- Menu ---")
        print("1. View Tasks")
        print("2. Add Standard Task")
        print("3. Add Timed Task (with Deadline)")
        print("4. Mark Task as Complete")
        print("5. Remove a Task")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            my_list.display_tasks()

        elif choice == "2":
            title = input("Enter task description: ").strip()
            if title:
                my_list.add_task(Task(title))
                print(f"Added task: '{title}'")
            else:
                print("Task description cannot be empty.")

        elif choice == "3":
            title = input("Enter task description: ").strip()
            # Default to an upcoming date for convenience, or let them input one
            print("Enter due date format as YYYY-MM-DD (e.g., 2026-06-15)")
            due_date = input("Enter due date: ").strip()
            
            if title and due_date:
                try:
                    my_list.add_task(TimedTask(title, due_date))
                    print(f"Added timed task: '{title}' (Due: {due_date})")
                except ValueError:
                    print("❌ Error: Invalid date format! Please use YYYY-MM-DD.")
            else:
                print("Both title and due date are required.")

        elif choice == "4":
            my_list.display_tasks()
            if not my_list.tasks:
                continue
                
            try:
                index = int(input("Enter the task number to complete: "))
                if 0 <= index < len(my_list.tasks):
                    print("\nCompleting task...")
                    # Polymorphism in action! Python decides which version to run.
                    my_list.tasks[index].mark_complete()
                else:
                    print("❌ Error: Task number out of range.")
            except ValueError:
                print("❌ Error: Please enter a valid number.")

        elif choice == "5":
            my_list.display_tasks()
            if not my_list.tasks:
                continue
                
            try:
                index = int(input("Enter the task number to remove: "))
                my_list.remove_task(index)
            except ValueError:
                print("❌ Error: Please enter a valid number.")

        elif choice == "6":
            print("\nGoodbye! Stay productive! 🚀")
            break

        else:
            print("❌ Invalid choice. Please pick a number from 1 to 6.")

if __name__ == "__main__":
    main()