import datetime

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.status = "Incomplete"
        self.priority = priority
        self.created_at = datetime.datetime.now()

    def mark_as_complete(self):
        self.status = "Complete"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(f"{task.description} - Priority: {task.priority} - Status: {task.status} - Created at: {task.created_at}")

# Your main application logic can go here

if __name__ == "__main__":
    # Example usage
    todo_list = ToDoList()

    task1 = Task("Complete Python project", "High")
    task2 = Task("Learn about classes", "Medium")

    todo_list.add_task(task1)
    todo_list.add_task(task2)

    todo_list.display_tasks()
