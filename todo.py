import json

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                tasks = [Task(**data) for data in tasks_data]
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            tasks_data = [task.__dict__ for task in self.tasks]
            json.dump(tasks_data, file)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task.completed else "Not Done"
            print(f"{i}. {task.description} - {status} (Due: {task.due_date})")

    def mark_task_completed(self, task_index):
        self.tasks[task_index].mark_completed()
        self.save_tasks()

    def remove_task(self, task_index):
        self.tasks.pop(task_index)
        self.save_tasks()

def display_menu():
    print("\n1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            task = Task(description, due_date)
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
