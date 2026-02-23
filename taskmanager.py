import tasks
import json

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return "Task removed successfully!"
        return "Sorry! Could not find that task..."
    
    def view_tasks(self):
        for task in self.tasks:
            print(task.summary())

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_complete()
                return "Task marked as complete!"
        return "Sorry! Could not find that task..."
            
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                task_data = json.load(file)
                for data in task_data:
                    task = tasks.Task(data["name"], data["description"], data["due_date"], data["priority"])
                    task.completed = data["completed"]
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No saved tasks found. Starting with an empty task list.")
            pass