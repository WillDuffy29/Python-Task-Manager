import taskmanager as tm
import tasks as t

manager = tm.TaskManager()
manager.load_tasks()

print("======================================================")
print("            Welcome to the Task Manager!")
print("======================================================")

while True:
  print("======================================================")
  print("Would you like to:")
  print("1. Add a task")
  print("2. Remove a task")
  print("3. View your tasks")
  print("4. Mark a task as complete")
  print("5. Exit")
  
  choice = int(input("Your selection: "))

  if choice == 1:
    print("Okay, let's add a task!")
    name = input("Task Name: ")
    description = input("Task Description: ")
    due_date = input("Task Due Date: ")
    priority = input("Task Priority: ")
    new_task = t.Task(name, description, due_date, priority)
    manager.add_task(new_task)
    print("Task added successfully!")
  
  elif choice == 2:
    print("Okay, let's remove a task!")
    name = input("Task Name: ")
    print(manager.remove_task(name))
  
  elif choice == 3:
    if manager.tasks == []:
      print("You have no tasks... Let's add some!")
    else:
      print("Here are your tasks:")
      manager.view_tasks()

  elif choice == 4:
    print("Okay, let's mark a task as complete!")
    name = input("Task Name: ")
    print(manager.complete_task(name))

  else:
    manager.save_tasks()
    print("Goodbye!")
    break