# Creating the class for the tasks

class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def completion(self):
        if self.completed == True:
            return "Task is complete!"
        else:
            return "In progress..."
    
    def summary(self):
        return f"Task: {self.name} | Description: {self.description} | Due Date: {self.due_date} | Priority: {self.priority} | Status: {self.completion()}"

# Example usage: task1 = Task("Learn HTML", "Learn the basics of HTML so you can move onto CSS and JavaScript", "31/03/2026", "High")